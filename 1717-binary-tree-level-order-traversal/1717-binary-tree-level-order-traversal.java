/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    //Three methods: 1. one queue, record size each time. 2. two queue, replace each other each time. 3.use dummmy node.
    //BFS has three ways to implement: 1.two queue 2.one queue + size 3.dummy node
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<TreeNode> queue = new ArrayList<TreeNode>();
        if(root == null)
            return res;
        else
            queue.add(root);

        while(!queue.isEmpty()){
            int size = queue.size();
            ArrayList<Integer> subRes = new ArrayList<Integer>();
            for(int i = 0; i< size; i++){
                TreeNode node = queue.remove(0);
                subRes.add(node.val);
                if(node.left != null)
                    queue.add(node.left);
                if(node.right != null)
                    queue.add(node.right);
            }
            res.add(subRes);
        }
        return res;
    }
}