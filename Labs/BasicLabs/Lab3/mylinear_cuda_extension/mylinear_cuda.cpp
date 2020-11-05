#include <torch/extension.h>

#include <iostream>
#include <vector>

// CUDA funciton declearition
std::vector<torch::Tensor> mylinear_cuda_forward(
    torch::Tensor input,
    torch::Tensor weights);

std::vector<torch::Tensor> mylinear_cuda_backward(
    torch::Tensor grad_output,
    torch::Tensor input,
    torch::Tensor weights); 

// C++ interface

#define CHECK_CUDA(x) TORCH_CHECK(x.type().is_cuda(), #x " must be a CUDA tensor")
#define CHECK_CONTIGUOUS(x) TORCH_CHECK(x.is_contiguous(), #x " must be contiguous")
#define CHECK_INPUT(x) CHECK_CUDA(x); CHECK_CONTIGUOUS(x)

std::vector<torch::Tensor> mylinear_forward(
    torch::Tensor input,
    torch::Tensor weights) 
{
    CHECK_INPUT(input);
    CHECK_INPUT(weights);

    return mylinear_cuda_forward(input, weights);
}

std::vector<torch::Tensor> mylinear_backward(
    torch::Tensor grad_output,
    torch::Tensor input,
    torch::Tensor weights) 
{
    CHECK_INPUT(grad_output);
    CHECK_INPUT(input);
    CHECK_INPUT(weights);

    return mylinear_cuda_backward(grad_output, input, weights);
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("forward", &mylinear_forward, "myLinear forward (CUDA)");
  m.def("backward", &mylinear_backward, "myLinear backward (CUDA)");
}
