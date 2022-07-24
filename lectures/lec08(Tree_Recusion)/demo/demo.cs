using System;

namespace RecurionApplication
{
    class Solution
    {
        /* factor */
        public int fact(int n)
        {
            // base case
            if(n == 0)
            {
                return 1;
            }
            return n * fact(n - 1);
        }

        /* cascade 
        cascade(1234) -->
        1234
        123
        12
        1
        12
        123
        1234
        */
        public void cascade(int n)
        {
            if(n < 10)
            {
                Console.WriteLine("{0}", n);
            }
            else
            {
                Console.WriteLine(n);
                cascade(n / 10);
                Console.WriteLine(n);
            }
        }

        /* inverse cascade
        inverse_cascade(1234)
        1
        12
        123
        1234
        123
        12
        1
        */
        private void grow(n)
        {
            if(n == 0) return;
            grow(n / 10);
            Console.WriteLine(n);
        }

        private void shrink(n)
        {
            if (n == 0) return;
            Console.WriteLine(n);
            shrink(n / 10);
        }

        public void inverse_cascade(int n)
        {
            // print grow sequence
            grow(n / 10);
            // print n
            Console.WriteLine(n);
            // print shrink sequence
            shrink(n / 10);
        }

        /* fib */
        public int fib(int n)
        {
            if(n == 0 || n == 1)
                return 1;
            return fib(n - 1) + fib(n - 2);
        }

        /* Hanoi */
        private void print_move(start, end)
        {
            Console.WriteLine("move the top of rod {0} to rod {1}", start, end);
        }

        public void move_stack(n, start, end)
        {
            // base case
            if (n == 1)
            {
                print_move(start, end);
            }

            int bridge = 6 - start - end;
            move_stack(n - 1, start, bridge);
            print_move(start, end);
            move_stack(n - 1, bridge, end);
        }

        static void Main(string[] args)
        {
            Solution s = new Solution();
            s.cascade(1234);
        }
    }
}