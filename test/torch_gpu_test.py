import unittest
import torch

print(torch.__version__)
print(torch.version.cuda)


class TestTorchGPU(unittest.TestCase):
    def test_gpu_availability(self):
        # Check if CUDA (GPU support) is available
        self.assertTrue(torch.cuda.is_available(), "CUDA is not available. GPU not detected.")

    def test_gpu_tensor_operation(self):
        if torch.cuda.is_available():
            # Perform a simple tensor operation on the GPU
            device = torch.device("cuda")
            tensor = torch.tensor([1.0, 2.0, 3.0], device=device)
            result = tensor * 2
            expected = torch.tensor([2.0, 4.0, 6.0], device=device)
            self.assertTrue(torch.allclose(result, expected), "Tensor operation on GPU failed.")
        else:
            self.skipTest("CUDA is not available. Skipping GPU tensor operation test.")


if __name__ == "__main__":
    unittest.main()