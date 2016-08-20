10 lockers.
More generally, for `n` lockers, `floor(sqrt(n))` lockers will remain open.

A locker will remain open at the end if it has been toggled an odd number of times.
The number of times a locker is toggled is equal to the number of factors that locker's number has (since it is only toggled on passes whose number evenly divides the locker number).
Most factors come in pairs, as factor `k` of number `n` will have a complementary factor `n/k`.
The only way a locker can be left with an odd number of factors is if `k` and `n/k` are the same, i.e., `n = k*k` or `n` is a perfect square.

The number of perfect squares between 1 and 100 is 10.