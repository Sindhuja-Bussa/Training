#include <stdio.h>

int main() {
    // Write C code here
    int l;
    scanf("%d",&l);
    int r=21;
    l<r?printf("required lemons=%d",r-l):l>r?printf("remaining lemons:%d",l-r):
    (l<='65' && l>='97')?printf("required lemons=%d",r-l)
    printf("sufficient lemons:%d",l);
    return 0;
}
