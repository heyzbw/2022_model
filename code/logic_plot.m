% 绘制逻辑回归预测值、真实值
% y_pre提前通过拖拽excel表单载入数据
y_fact = [1 1 1 1 1 1  0 0 0 0 0 0 0 0 0 0 0 0 0 0];
x= linspace(1,20,20);
plot(x,y_pre)
hold on 
plot(x,y_fact)

legend('模型预测值','实际值')