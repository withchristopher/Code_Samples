//Assignment 1 - first time I have used c to program!
// Not able to resolve power function for cipher, used brute-force method for multiplication.
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void matthews(float x[], int n, float key);
float keygen(int NM);
void binary(int b);
void encrypt(float key);
void decrypt(float key);

int main()
{
  //Parameters
  int SIZE =20;//Size of array
  float x[SIZE];//x[n]
  int N=10;// N array
  int M=15;// M array
  float k;//Key
  float i; //Iterate over i
  //printf("Array Size:%d%f",N,k)
  

  //Generate x0 keys between 0 & 1.
  float keygen(int NM)
  {
    for(i=0.1;i<1;i+=0.1)
      {
	matthews(x,NM,i);
      }
    return;
  }
  //Lyapunov Dimension
  float sn[SIZE],sm[SIZE];
  sn[N] =keygen(N);//Sigma N
  sm[M] =keygen(M);//Sigma M
  if (sn[N]<sm[M])
    printf("Lyapunov Dim (Sigma N < Sigma M): %f\n",(1-(sn[N]/sm[M])));
  else
    printf("Lyapunov Dim (Sigma N > Sigma M: %f\n",(1-(sm[M]/sn[N])));
  //Encrypt
  //Enter code(bank code) to be converted into binary
  int g;
  printf("Enter your code:");
  scanf("%d",&g);
  binary(g);
  printf("\n"); 
  return;
}
//Generate different KEYS between 

//MATTHEWS Cipher Void Function - does not use a power function but uses brute force for r=4.
void matthews(float x[], int n, float key)
{
  int i;
  for (i=0;i<n;i++)
    {
      int r=4;
      x[0]=key;
      x[i+1]=(1+r)*((1+1/r)*(1+1/r)*(1+1/r)*(1+1/r))* x[i]*((1- x[i])*(1- x[i])*(1- x[i])*(1- x[i]));
      //printf("Key:%f. Number:%d. Output:%f\n",key,n,x[i+1]);
    }
  //Lyapunov exponent
  for (i=1;i<n;i++)
    {
      float s[n];
      s[i+1]+=(1/n)*(log,2,(abs, x[i+1]/ x[i]));
      //printf("Lya:%f\n",x[i+1]);
    }
  return;
}

void binary(int b)
{
  /* step 1 */
  if (b > 1)
    binary(b/2);
  
  /* step 2 */
  printf("%d", b % 2);
}
