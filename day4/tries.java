public class Solution {

    // implement a trie and use it to efficiently store string
    
    static class Node
    {
        Node radix[];
        boolean end;
        
        Node()
        {
            radix= new Node[26];
            end=false;
        }
    }

    static class Trie {
        
        Node parent = new Node();

        public boolean addWord(String word) {
            System.out.println(word);
            Node root= new Node();
            root=parent;
            for(int i=0;i<word.length();i++)
            {
                int index=(int)word.charAt(i)-'a';
                if(root.radix[index]==null)
                {
                    root.radix[index]= new Node();
                    root=root.radix[index];
                }
                else
                {
                    root=root.radix[index];
                }
            }
            if(root.end==false)
            {
                root.end=true;
                return true;
            }
            return false;
        }
    }

