#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *secondHalf;
	int palindrome = 1;

	/* Find the center of the list */
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast == NULL)
		secondHalf = slow;
	else
		secondHalf = slow->next;

	/* Reverse the second half of the list */
	slow = NULL;
	while (secondHalf != NULL)
	{
		fast = secondHalf->next;
		secondHalf->next = slow;
		slow = secondHalf;
		secondHalf = fast;
	}
	secondHalf = slow;

	/* Compare the first and second parts */
	slow = *head;
	fast = secondHalf;
	while (slow && fast)
	{
		if (slow->n != fast->n)
		{
			palindrome = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}
	/* Reverse the second part and link it back to the first part */
	slow = NULL;
	while (secondHalf != NULL)
	{
		fast = secondHalf->next;
		secondHalf->next = slow;
		slow = secondHalf;
		secondHalf = fast;
	}
	secondHalf = slow;
	/* Return the result */
	return palindrome;
}
