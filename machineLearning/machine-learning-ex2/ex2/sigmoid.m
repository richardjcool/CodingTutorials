function g = sigmoid(z)
%SIGMOID Compute sigmoid functoon
%   J = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

zSize = size(z);
for i = 1:zSize(1)
    for j = 1:zSize(2)
        g(i,j) = 1.0 / ( 1.0 + exp(-1.0*z(i,j)));
    end
end




% =============================================================

end
