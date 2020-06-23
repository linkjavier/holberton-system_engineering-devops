#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_loop - Enter in a infinite loop.
 *
 * Return: always 0 (success)
 */

int infinite_loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: always 0 (success)
 */
int main(void)
{
	pid_t pid;
	unsigned int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid < 0)
			perror("fork error");
		else if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %ld\n", (long) pid);
		i++;
	}
	infinite_loop();
	return (0);
}
