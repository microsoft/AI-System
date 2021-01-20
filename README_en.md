# AI-System

[简体中文](./README.md)

This is an online AI System Course to help students learn the whole stack of systems that support AI, and practice them in the real projects. In this course, we will use terms **AI-System** and **System for AI** alternately. 

This course is one of the AI-related course in [微软人工智能教育与共建社区](https://github.com/microsoft/ai-edu). Under the [A-基础教程](https://github.com/microsoft/ai-edu/tree/master/A-%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B) module. The course numbe an name are *A6-人工智能系统*.

Welcome to [A-基础教程](https://github.com/microsoft/ai-edu/tree/master/A-%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B) module to access more related content.

It is strongly recommended that learners who want to learn or consolidate the core knowledge of artificial intelligence, first learn [A2-神经网络基本原理简明教程](https://aka.ms/beginnerAI)，also known as the **9-step learn Neural Network**。It will bring great help to the study of this course.

## Background

In recent years, the rapid development of artificial intelligence, especially deep learning technology, is inseparable from the continuous progress of hardware and software systems. In the foreseeable future, the development of artificial intelligence technology will still rely on a joint innovation model that combines computer systems and artificial intelligence. Computer systems are now empowering artificial intelligence with a larger scale and higher complexity. This requires not only more system innovation, but also systematic thinking and methodology. At the same time, artificial intelligence in turn provides support for the design of complex systems.

We have noticed that most of the current artificial intelligence-related courses, especially deep learning and machine learning related courses, mainly focus on related theories, algorithms or applications, but system-related courses are rare. We hope that the course of artificial intelligence systems can make artificial intelligence related education more comprehensive and in-depth, so as to jointly promote the cultivation of talents that intersect artificial intelligence and systems.


## Purpose

This course aims to help students:

1. Completely understand the computer system architecture that supports deep learning, and learn the system design under the full life cycle of deep learning through practical problems.

2. Introduce cutting-edge systems and artificial intelligence research work, including AI for Systems and Systems for AI, to help senior undergraduates and graduate students better find and define meaningful research questions.

3. Design experimental courses from the perspective of system research. Encourage students to implement and optimize system modules by operating and applying mainstream and latest frameworks, platforms and tools to improve their ability to solve practical problems, not just understanding the use of tools.

**Prerequisites:** C/C++/Python, Computer Architecture, Introduction to algorithms

## Characteristic

The course mainly includes the following three modules:

The first part is the basic knowledge of artificial intelligence and a full-stack overview of artificial intelligence systems; and the systematic design and methodology of deep learning systems. 

The second part of the advanced courses includes the most cutting-edge systems and artificial intelligence research fields. 

The third part is the supporting experimental courses, including the most mainstream frameworks, platforms and tools, and a series of experimental projects.

The content of the first part will focus on basic knowledge, while the content of the other two parts will be dynamically adjusted with the technological progress of academia and industry. The content of the latter two parts will be organized in a modular form to facilitate adjustment or combination with other CS courses (such as compilation principles, etc.) as advanced lectures or internship projects.

The design of this course will also draw on the research results and experience of Microsoft Research Asia in the intersection of artificial intelligence and systems, including some platforms and tools developed by Microsoft and the research institute. The course also encourages other schools and teachers to add and adjust more advanced topics or other experiments according to their needs.

## Syllabus

### [Lectures](./Lectures)

Lectures have two parts--basic courses and advanced courses. The first part is focus on basic theories, from lesson 1 to 6, while the second part involves more cutting-edge research, from lesson 7 to 14.

*Basic Courses*
| | | |
|---|---|---|
| Course No.|Lecture Name|Remarks|
|1|Introduction|Overview and system/AI basics|
|2|System perspective of Systems for AI|Systems for AI: a historic view; Fundamentals of neural networks; Fundamentals of Systems for AI|
|3|Computation frameworks for DNN|Backprop and AD, Tensor, DAG, Execution graph. <br>Papers and systems: PyTorch, TensorFlow|
|4|Computer architecture for Matrix computation|Matrix computation, CPU/SIMD, GPGPU, ASIC/TPU <br>Papers and systems: Blas, TPU|
|5|Distributed training algorithms|Data parallelism, model parallelism, distributed SGD <br>Papers and systems: PipeDream|
|6|Distributed training systems|MPI, parameter servers, all-reduce, RDMA <br>Papers and systems: Horovod|
|7|Scheduling and resource management system|Running dnn job on cluster: container, resource allocation, scheduling <br>Papers and systems: Kubeflow, OpenPAI,Gandiva, HiveD|
|8|Inference systems|Efficiency, latency, throughput, and deployment <br>Papers and systems: TensorRT, TensorflowLite, ONNX|
||||


*Advanced Courses*
| | | |
|---|---|---|
| Course No.|Course Name|Remarks|
|9|Computation graph compilation and optimization|IR, sub-graph pattern match, Matrix multiplication and memory optimization <br>Papers and systems: XLA, MLIR, TVM, NNFusion|
|10|Efficiency via compression and sparsity|Model compression, Sparsity, Pruning|
|11|AutoML systems|Hyper parameter tuning, NAS <br>Papers and systems: Hyperband, SMAC, ENAS, AutoKeras, NNI|
|12|Reinforcement learning systems|Theory of RL, systems for RL <br>Papers and systems: AC3, RLlib, AlphaZero|
|13|Security and Privacy|Federated learning, security, privacy <br>Papers and systems: DeepFake|
|14|AI for systems|AI for traditional systems problems, for system algorithms <br>Papers and systems: Learned Indexes, Learned query path|
||||


### [Labs](./Labs)
Labs also have two parts: The first part is configured to make sure students can run most of Labs at local machine. The advanced part may need a small cluster (local or on Cloud) with GPU support.

*Basic Labs*
||||
|---|---|---|
|<div style="width:50px">Lab No.</div>|Lab Name|Remarks|
|Lab 1|A simple end-to-end AI example, <br>from a system perspective|Understand the systems from debug info and system logs
|Lab 2|Customize operators|Design and implement a customized operator (both forward and backward) in python|
|Lab 3|CUDA implementation|Add a CUDA implementation for the customized operator|
|Lab 4|AllReduce implementation|Improve AllReduce on Horovod: implement a lossy compression (3LC) on GPU for low-bandwidth network|
|Lab 5|Configure containers for customized training and inference|Configure containers|
||||

*Advanced Labs*
||||
|---|---|---|
|<div style="width:50px">Lab No.</div>|Lab Name|Remarks|
|Lab 6|Scheduling and resource management system|Get familiar with OpenPAI or KubeFlow|
|Lab 7|Distributed training|Try different kinds of all reduce implementations|
|Lab 8|AutoML|Search for a new neural network structure for Image/NLP tasks|
|Lab 9|RL Systems|Configure and get familiar with one of the following RL Systems: RLlib, …|
||||

## appendix

The following lists the relevant courses in the direction of artificial intelligence systems in other schools and institutions.

\<TBD>

---

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
