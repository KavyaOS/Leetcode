class Solution {
    public int removeElement(int[] nums, int val) {
        int n=nums.length,temp=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]!=val)
            {
                nums[temp++]=nums[i];
            }

        }
        return temp;
    }
}
public class main()
{
    public static void main(String args[])
    {
        Solution solution=new Solution();
        int[] num = new int[]{0,1,2,2,3,0,4,2};
        solution.removeElement(num,2);
    }
}