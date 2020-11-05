#include <torch/extension.h>

#include <iostream>
#include <vector>

std::vector<torch::Tensor> mylinear_forward(
    torch::Tensor input,
    torch::Tensor weights) 
{
    auto output = torch::mm(input, weights.transpose(0, 1));
    
    return {output};
}

std::vector<torch::Tensor> mylinear_backward(
    torch::Tensor grad_output,
    torch::Tensor input,
    torch::Tensor weights
    ) 
{
    auto grad_input = torch::mm(grad_output, weights);
    auto grad_weights = torch::mm(grad_output.transpose(0, 1), input);

    return {grad_input, grad_weights};
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("forward", &mylinear_forward, "myLinear forward");
  m.def("backward", &mylinear_backward, "myLinear backward");
}
