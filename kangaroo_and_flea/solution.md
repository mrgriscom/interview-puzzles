Yes, the flea catches up to the kangaroo.
It will do so (eventually) no matter the size of its jump in proportion to the kangaroo.

Let `J_k` be the size of the kangaroo's jump (`1 m`), and `J_f` be that of the flea (`1 cm`).
Also let `F_n` be the distance of the flea from the pole after jump `n`, and likewise `K_n` for the kangaroo:

`K_n = n * J_k`

- `F_1 = J_f`
- `F_n = K_n/K_(n-1) * F_(n-1) + J_f`

The first few iterations of the flea's position look like:

- `F_1 = J_f`
- `F_2 = 2/1 * J_f + J_f`
- `F_3 = 3/2 * (2/1 * J_f + J_f) + J_f`
- `F_4 = 4/3 * (3/2 * (2/1 * J_f + J_f) + J_f) + J_f`

and expanding, we get:

- `F_1 = J_f * 1`
- `F_2 = J_f * (2/1 + 1)`
- `F_3 = J_f * (3/1 + 3/2 + 1)`
- `F_4 = J_f * (4/1 + 4/2 + 4/3 + 1)`

Thus `F_n = J_f * sum(n/i for i from 1 to n)`, and the flea's distance as a proportion of the kangaroo's (which, if exceeding `1`, means the flea has caught up) is:

`F_n/K_n = J_f * sum(n/i for i from 1 to n) / (n * J_k) = J_f/J_k * sum(1/i for i from 1 to n)`

`sum(1/i for i from 1 to n)` is the harmonic series, which diverges, so this formula will always exceed `1` for sufficiently large `n`.
Therefore, the flea always catches up to the kangaroo.

How long will it take?

`harmonic_sum(n)` can be roughly approximated as `ln(n)`, making the number of jumps to catch up `e^(J_k/J_f)`.

For a flea-kangaroo jump ratio of `1:100`, this yields `2.7e43 m`.
The observable universe is "only" `8.8e23` m across.