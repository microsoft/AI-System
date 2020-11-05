import logging
import random
import sys
from collections import OrderedDict

import numpy as np
import torch


def reset_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    try:
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
    except:
        # maybe not available
        pass


def prepare_logger(args):
    time_format = '%m/%d %H:%M:%S'
    fmt = '[%(asctime)s] %(levelname)s (%(name)s) %(message)s'
    formatter = logging.Formatter(fmt, time_format)
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


def accuracy(outputs, targets):
    _, predict = torch.max(outputs.data, 1)
    correct = predict.eq(targets.data).cpu().sum().item()
    return correct / outputs.size(0)


class AverageMeterGroup:
    """Average meter group for multiple average meters"""

    def __init__(self):
        self.meters = OrderedDict()

    def update(self, data, n=1):
        for k, v in data.items():
            if k not in self.meters:
                self.meters[k] = AverageMeter(k, ':4f')
            self.meters[k].update(v, n=n)

    def __getattr__(self, item):
        return self.meters[item]

    def __getitem__(self, item):
        return self.meters[item]

    def __str__(self):
        return '  '.join(str(v) for v in self.meters.values())

    def summary(self):
        return '  '.join(v.summary() for v in self.meters.values())

    def average_items(self):
        return {k: v.avg for k, v in self.meters.items()}


class AverageMeter:
    """Computes and stores the average and current value"""

    def __init__(self, name, fmt=':f'):
        """
        Initialization of AverageMeter
        Parameters
        ----------
        name : str
            Name to display.
        fmt : str
            Format string to print the values.
        """
        self.name = name
        self.fmt = fmt
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

    def __str__(self):
        fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
        return fmtstr.format(**self.__dict__)

    def summary(self):
        fmtstr = '{name}: {avg' + self.fmt + '}'
        return fmtstr.format(**self.__dict__)
