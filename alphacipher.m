%Cipher 1 -
function alphacipher(x,n,a)
x=size(n);
r=1;
for i=1:n
    x(1)=a;
    x(i+1)= r*x(i)*(1-x(i))^(3*r)-tan(r/100);
end

N=100;
M=200;
key=size(abs(N-M)/(N+M));
for i=1:key:0.1
    w1(i+1)=alphacipher(x,N,key);
    w2(i+1)=alphacipher(x,M,key);
end

for i=1:N
    sn(i)=(1/N)*(sum(log(abs(w(i+1)/w(i)))));
end
for i=1:M
    sm(i)=(1/M)*(sum(log(abs((w2(i+1)/w2(i))))));
end
if (sm > sn)
      dl=(1-(sn/sm))
else
      dl=(1-(sm/sn))
end
subplot(2,1,1), plot(sn); 
subplot(2,2,1), plot(sm);
h=hist(sn,32);
subplot(2,1,2), bar(h);
pause;
end;
