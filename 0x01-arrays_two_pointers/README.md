# Arrays - Two Pointers

1. [0-isPalindrome.py](0-isPalindrome.py)- [Leetcode 125](https://leetcode.com/problems/valid-palindrome/description/): A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string ```s```, return ```true``` if it is a palindrome, or ```false``` otherwise.

2. [1-search](1-search.py) - [Leetcode 704](https://leetcode.com/problems/binary-search/description/): Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return ```-1```. You must write an algorithm with ```O(log n)``` runtime complexity.

3. [2-removeDuplicates.py](2-removeDuplicates.py) - [Leetcode 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/): Given an integer array ```nums``` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Consider the number of unique elements in nums to be ```k​​​​​​​​​​​​​```​. After removing duplicates, return the number of unique elements ```k```. The first ```k``` elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index ```k - 1``` can be ignored.

4. [3-removeElement.py](3-removeElement.py) -[leetcode 27](https://leetcode.com/problems/remove-element/description/): Given an integer array ```nums``` and an integer ```val```, remove all occurrences of ```val``` in nums in-place. The order of the elements may be changed. Then return the number of elements in ```nums``` which are not equal to ```val```. Consider the number of elements in ```nums``` which are not equal to ```val`` be ```k```, to get accepted, you need to do the following things: Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return ```k```.

5. [4-twoSum.py](4-twoSum.py) - [Leetcode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) - Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be ```numbers[index1]``` and ```numbers[index2]``` where ```1 <= index1 < index2 <= numbers.length```.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.