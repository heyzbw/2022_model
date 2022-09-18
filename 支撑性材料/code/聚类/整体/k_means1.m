clc; close all; clear;
[num]=xlsread('element.xlsx')
data=num; 
N=4;%设置聚类数目
[m,n]=size(data);
pattern=zeros(m,n+1);
center=zeros(N,n);%初始化聚类中心
pattern(:,1:n)=data(:,:);
for x=1:N
    center(x,:)=data( randi(49,1),:);%第一次随机产生聚类中心
end
figure('name','聚类过程');
while 1
distence=zeros(1,N);
num=zeros(1,N);
new_center=zeros(N,n);
 
%loop draw figure

drawfigure(pattern,center)
for x=1:m                             %该循环对每一个点分别计算到中心的距离，然后按照最近的那个中心进行归类。
    for y=1:N
    distence(y)=norm(data(x,:)-center(y,:));%计算到每个类的距离,看看某一个点到这三个中心哪一个点最近
    end
    [~, temp]=min(distence);%求最小的距离,忽略第一个最小值具体数值，我只取第二个参数即最小值所在的索引
    pattern(x,n+1)=temp;         
end
k=0;
for y=1:N
    for x=1:m
        if pattern(x,n+1)==y                %如果当前点属于第y个中心
           new_center(y,:)=new_center(y,:)+pattern(x,1:n);  %就对第y个中心（x,y）求和相加
           num(y)=num(y)+1;                 %对第y个中心自增，主要是为了求均值。
        end
    end
    new_center(y,:)=new_center(y,:)/num(y); %求取聚类中心的均值
    if norm(new_center(y,:)-center(y,:))<0.1    %当有一个聚类中心没有发生太大变化时，说明该点就是中心点了。当聚集了N个中心没有点时，那么就可以结束运算了
        k=k+1;
    end
end
if k==N
     break;
else
     center=new_center;
end
end
[m, n]=size(pattern);
 
%最后显示聚类后的数据
figure;
hold on
for i=1:m
    if pattern(i,n)==1 
         plot(pattern(i,1),pattern(i,2),'r*');
         plot(center(1,1),center(1,2),'ko');
    elseif pattern(i,n)==2
         plot(pattern(i,1),pattern(i,2),'g*');
         plot(center(2,1),center(2,2),'ko');
    elseif pattern(i,n)==3
         plot(pattern(i,1),pattern(i,2),'b*');
         plot(center(3,1),center(3,2),'ko');
    elseif pattern(i,n)==4
         plot(pattern(i,1),pattern(i,2),'y*');
         plot(center(4,1),center(4,2),'ko');
%     elseif pattern(i,n)==5
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(5,1),center(5,2),'ko');
%     elseif pattern(i,n)==6
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(6,1),center(6,2),'ko');
%     elseif pattern(i,n)==7
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(7,1),center(7,2),'ko');
%     elseif pattern(i,n)==8
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(8,1),center(8,2),'ko');
%     elseif pattern(i,n)==9
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(9,1),center(9,2),'ko');
%     elseif pattern(i,n)==10
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(10,1),center(10,2),'ko');
%     elseif pattern(i,n)==11
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(11,1),center(11,2),'ko');
%     elseif pattern(i,n)==12
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(12,1),center(12,2),'ko');
%     elseif pattern(i,n)==13
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(13,1),center(13,2),'ko');
%     elseif pattern(i,n)==14
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(14,1),center(14,2),'ko');
%     elseif pattern(i,n)==15
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(15,1),center(15,2),'ko');
    else
         plot(pattern(i,1),pattern(i,2),'m*');
         plot(center(4,1),center(4,2),'ko');
    end
end     
grid on;


function drawfigure(pattern,center)
[m, n]=size(pattern);

hold on;
for i=1:m
    if pattern(i,n)==1 
         plot(pattern(i,1),pattern(i,2),'r*');
         plot(center(1,1),center(1,2),'ko');
    elseif pattern(i,n)==2
         plot(pattern(i,1),pattern(i,2),'g*');
         plot(center(2,1),center(2,2),'ko');
    elseif pattern(i,n)==3
         plot(pattern(i,1),pattern(i,2),'b*');
         plot(center(3,1),center(3,2),'ko');
    elseif pattern(i,n)==4
         plot(pattern(i,1),pattern(i,2),'y*');
         plot(center(4,1),center(4,2),'ko');
%     elseif pattern(i,n)==5
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(5,1),center(5,2),'ko');
%     elseif pattern(i,n)==6
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(6,1),center(6,2),'ko');
%     elseif pattern(i,n)==7
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(7,1),center(7,2),'ko');
%     elseif pattern(i,n)==8
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(8,1),center(8,2),'ko');
%     elseif pattern(i,n)==9
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(9,1),center(9,2),'ko');
%     elseif pattern(i,n)==10
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(10,1),center(10,2),'ko');
%     elseif pattern(i,n)==11
%          plot(pattern(i,1),pattern(i,2),'g*');
%          plot(center(11,1),center(11,2),'ko');
%     elseif pattern(i,n)==12
%          plot(pattern(i,1),pattern(i,2),'b*');
%          plot(center(12,1),center(12,2),'ko');
%     elseif pattern(i,n)==13
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(13,1),center(13,2),'ko');
%     elseif pattern(i,n)==14
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(14,1),center(14,2),'ko');
%     elseif pattern(i,n)==15
%          plot(pattern(i,1),pattern(i,2),'y*');
%          plot(center(15,1),center(15,2),'ko');
    else
         plot(pattern(i,1),pattern(i,2),'m*');
         plot(center(4,1),center(4,2),'ko');
    end
    
end
hold off;
pause(0.7);
clf
end