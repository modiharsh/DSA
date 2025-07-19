# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem #Medium #Array #String

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # My original solution
        # folder.sort()
        # folder_set = set()
        # res = []
        # for f in folder:
        #     if f == "/" or f == "":
        #         continue
        #     curr = f
        #     flag = True
        #     while curr:
        #         last_folder_index = curr.rfind('/')
        #         if last_folder_index < 0:
        #             break
        #         parent = curr[:last_folder_index]
        #         curr = curr[:last_folder_index]
        #         if parent in folder_set:
        #             flag = False
        #             break

        #     if not flag:
        #         continue
        #     else:
        #         res.append(f)
        #         folder_set.add(f)
        # return res

        # Neater solution
        folder.sort()
        res = []

        for f in folder:
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)
        
        return res

        # Using optimized method of using Trie node
        # class TrieNode:
        #     def __init__(self):
        #         self.children = {}
        #         self.is_end = False
                
        # folder.sort()
        # root = TrieNode()
        # res = []

        # for path in folder:
        #     node = root
        #     path_parts = path.split("/")[1:]
        #     should_add = True

        #     for part in path_parts:
        #         if node.is_end:
        #             should_add = False
        #             break

        #         if part not in node.children:
        #             node.children[part] = TrieNode()
        #         node = node.children[part]

        #     if should_add:
        #         res.append(path)
        #         node.is_end = True

        # return res




# Example 1:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
# Example 2:

# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
# Example 3:

# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
