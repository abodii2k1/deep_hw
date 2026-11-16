r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. **False.** A useful split needs both subsets to be representative of the same
distribution, and each needs to be large enough. For example, if the data is
sorted by class and we take the last 20% as the test set,
the test set may contain only one or two classes, so it measures performance on
a distribution the model was not trained on.

2. **False.** Cross-validation is part of model selection, so the test set must be 
held out until the very end and used only once, for the final estimate of the generalization error.

3. **False.** The validation score of a single fold is a noisy estimation, because
it is computed on a small subset. The proxy for generalization error is the error on the
held-out test set, measured after retraining the selected model on the full training set.

4. **False.** To check if a model is robust, we change the inputs a little
(for example, add noise to the images) and see if the model still predicts
the right answers. Adding noise to the labels does not test this. If some
labels are wrong, a correct prediction can be counted as a mistake, so the
score no longer tells us how good the model really is.

"""

part1_q2 = r"""
**Your answer:**

**No, the approach is not justified.** By trying several values of $\lambda$ and
keeping the one with the best test-set result, the friend used the test set for
model selection, so $\lambda$ is now a hyperparameter fit to the test set. The
test set is a part of the training process, and the reported test
error is biased: the selected $\lambda$ may simply fit the
particular test samples well rather than generalize.

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**

If $\Delta < 0$, the loss no longer asks the correct class to have the highest
score. The hinge term $\max(0, \Delta + s_j - s_{y_i})$ is zero whenever
$s_{y_i} - s_j > \Delta$. With a negative $\Delta$, this holds even when the
wrong class $j$ scores higher than the correct class, as long as it is higher
by less than $|\Delta|$. So some misclassifications cost nothing.

"""

part2_q2 = r"""
**Your answer:**

The score for class $j$ is the inner product $\vec{w_j}\vec{x}$, so each weight
vector, shown as an image, acts as a template for its digit. Bright
(positive) pixels are where strokes of this digit usually appear, so ink there
raises the score. Dark (negative) pixels are where strokes of other digits
usually appear, so ink there lowers the score. We can also see blury shapes of each digit,
which is because the model learns the average picture of each digit and classifies a sample
by how much its pixels overlap with each template.

"""

part2_q3 = r"""
**Your answer:**

1. **Good.** The training loss drops quickly in the first few epochs and then
decreases more and more slowly, flattening out smoothly by the end of training,
with no jumps. This means training has converged in the given number of
epochs.

2. **Slightly overfitted to the training set.** The model reaches a little over 95%
accuracy on the training set but about 89% on the test set, a gap of about
6 percentage points. The model performs better on data it was trained on than
on unseen data, which is the definition of overfitting. However, the
overfitting is only slight.

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
