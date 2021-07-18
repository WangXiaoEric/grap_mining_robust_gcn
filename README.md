# grap_mining_robust_gcn
在之前计算loss_diffiential =  loss_fro + args.gamma \* loss_gcn + args.lambda_ \* loss_smooth_feat + args.phi \* loss_symmetric的时候，是无法将gamma, lambda_, phi统一放到模型中反向计算梯度，否则算出来的参数一定是越小越好。

在Main中建模，a\*gamma^2 + b\*lambda_^2 + c\*phi^2， 将三个参数gamma, lambda_, phi按照步进的方式，进行多次训练（譬如1000次），保留ACC。
在对模型中a,b,c参数进行拟合求解，找到曲线中ACC最大值对应的参数作为Pro-GCN的实际使用参数；



Before calculating loss_diffiential = loss_fro + args.gamma * loss_gcn + args.lambda_ * loss_smooth_feat + args.phi * Under LOSS_SYMMETRIC, 
it is impossible to put Gamma, lambda_ and phi into the model to calculate the gradient. As the parameters to be calculated must be as small as possible.
Model in Main,  a\*gamma^2 + b\*lambda_^2 + c\*phi^2, gamma, lambda_, phi, step by step, and train many times (say 1000 times), leaving ACC.
The parameters A, B and C in the model were fitted and solved, and the parameters corresponding to the maximum value of ACC in the curve were found as the actual parameters used by Pro-GCN.

$x_i^2$
