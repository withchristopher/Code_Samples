#include <stdio.h>
#include <math.h>
#include <string.h>

void elowin(char z, int r, int num);
void elostatus(char x, int e, int nm);

//Main Program
main()
{
  int w;
  int rt; //Rating
  int gp; //Games Played
  char a; //Player code

  printf("Enter your name:");
  scanf("%s",&a);
  printf("Enter the your opponents rating:");
  scanf("%d",&rt);
  printf("Enter the number of games you intend to play:");
  scanf("%d",&gp);
  elostatus(a,rt,gp);
  // elowin(a,rt,gp);

}
//Void functions
void elowin(char z, int r, int num) //Num=number of games, r=rating
{
  int rate;
  if (r>0)
    {
      rate=((r+400)/num);
      printf("%c 's rating: %d\n",z,rate);
    }
  return;
}

void elostatus(char x, int e, int nm)
{
  int rating;
  if(e>0)
    {
      if (x ='w')
	{
	  rating=(((nm*e)+400)/nm);
	  printf("Win, new Rating: %d\n",rating);
	}
      if (x='l')
	{
	  rating =(((nm*e)-400)/nm);
	  printf("Loss, new Rating: %d\n",rating);
	}
      if (x='d')
	{
	  rating=((nm*e)/nm);
	  printf("Draw, new Rating: %d\n",rating);
	}	  
      else
	printf("Unknown letter, please run again\n");
      //printf("%c\n",x);
    }
  return;
}
