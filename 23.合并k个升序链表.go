/*
 * @lc app=leetcode.cn id=23 lang=golang
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
	if lists == nil {
		return nil
	}
	arr := make([]int, 0)
	for _, l := range lists {
		if l == nil {
			continue
		}
		for l != nil {
			arr = append(arr, l.Val)
			l = l.Next
		}
	}
	sort.Ints(arr)
	ans := &ListNode{}
	head := ans
	for _, n := range arr {
		node := &ListNode {Val: n,}
		head.Next = node
		head = head.Next
	}
	return ans.Next

}
// @lc code=end

