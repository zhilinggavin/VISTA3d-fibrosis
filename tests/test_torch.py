import unittest
import torch

class TestTorchDevice(unittest.TestCase):
    def setUp(self):
        # Automatically select GPU if available, otherwise use CPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def test_device_availability(self):
        # Check if the selected device is valid
        self.assertIn(self.device.type, ["cuda", "cpu"], "Invalid device type detected.")
        print(f"Torch Version: {torch.__version__}")
        print(f"Using device: {self.device}")

    def test_tensor_operation(self):
        # Perform a simple tensor operation on the selected device
        tensor = torch.tensor([1.0, 2.0, 3.0], device=self.device)
        result = tensor * 2
        expected = torch.tensor([2.0, 4.0, 6.0], device=self.device)
        self.assertTrue(torch.allclose(result, expected), "Tensor operation failed on the selected device.")


if __name__ == "__main__":
    unittest.main()