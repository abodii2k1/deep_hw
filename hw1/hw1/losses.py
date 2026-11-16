import abc
import torch


class ClassifierLoss(abc.ABC):
    """
    Represents a loss function of a classifier.
    """

    def __call__(self, *args, **kwargs):
        return self.loss(*args, **kwargs)

    @abc.abstractmethod
    def loss(self, *args, **kw):
        pass

    @abc.abstractmethod
    def grad(self):
        """
        :return: Gradient of the last calculated loss w.r.t. model
            parameters, as a Tensor of shape (D, C).
        """
        pass


class SVMHingeLoss(ClassifierLoss):
    def __init__(self, delta=1.0):
        self.delta = delta
        self.grad_ctx = {}

    def loss(self, x, y, x_scores, y_predicted):
        """
        Calculates the Hinge-loss for a batch of samples.

        :param x: Batch of samples in a Tensor of shape (N, D).
        :param y: Ground-truth labels for these samples: (N,)
        :param x_scores: The predicted class score for each sample: (N, C).
        :param y_predicted: The predicted class label for each sample: (N,).
        :return: The classification loss as a Tensor of shape (1,).
        """

        assert x_scores.shape[0] == y.shape[0]
        assert y.dim() == 1

        # TODO: Implement SVM loss calculation based on the hinge-loss formula.
        #  Notes:
        #  - Use only basic pytorch tensor operations, no external code.
        #  - Full credit will be given only for a fully vectorized
        #    implementation (zero explicit loops).
        #    Hint: Create a matrix M where M[i,j] is the margin-loss
        #    for sample i and class j (i.e. s_j - s_{y_i} + delta).

        # ====== YOUR CODE: ======
        N, C = x_scores.shape
        correct_scores = x_scores[torch.arange(N), y].unsqueeze(1)

        M = x_scores - correct_scores + self.delta

        is_correct = torch.arange(C).unsqueeze(0) == y.unsqueeze(1)

        hinge = torch.clamp(M, min=0) * (~is_correct)
        loss = hinge.sum() / N
        # ========================

        # TODO: Save what you need for gradient calculation in self.grad_ctx
        # ====== YOUR CODE: ======
        self.grad_ctx["x"] = x
        self.grad_ctx["M"] = M.detach()
        self.grad_ctx["is_correct"] = is_correct
        # ========================

        return loss

    def grad(self):
        """
        Calculates the gradient of the Hinge-loss w.r.t. parameters.
        :return: The gradient, of shape (D, C).

        """
        # TODO:
        #  Implement SVM loss gradient calculation
        #  Same notes as above. Hint: Use the matrix M from above, based on
        #  it create a matrix G such that X^T * G is the gradient.

        # ====== YOUR CODE: ======
        x = self.grad_ctx["x"]
        M = self.grad_ctx["M"]
        is_correct = self.grad_ctx["is_correct"]
        N = x.shape[0]

        # Wrong classes: 1 where the margin is violated (m_ij > 0), else 0
        G = ((M > 0) & ~is_correct).float()

        # Correct class: minus the number of violated margins in that row
        G = G - is_correct.float() * G.sum(dim=1, keepdim=True)

        grad = x.T @ G / N
        # ========================

        return grad
