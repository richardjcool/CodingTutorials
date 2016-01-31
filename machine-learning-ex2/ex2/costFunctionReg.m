function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


model = sigmoid(theta'*X')';

sumSquareTheta = 0;
%We starte at 2 since theta0 (1 here with indexing) isn't Regularlized
for i = 2:size(theta)
    sumSquareTheta = sumSquareTheta + theta(i)^2;
end

regTerm = lambda / (2*m) * sumSquareTheta;

J = 1/m * sum(-1.0*y.*log(model)-(1.0-y).*log(1.0-model)) + regTerm;

grad(1) = 1/m * sum( (model-y).*X(:,1));
for i = 2:size(theta)
    grad(i) = 1.0 / m * sum( (model-y).*X(:,i)) + lambda/m*theta(i);
end


% =============================================================

end
