---
title: "Nonsingularity of a Logarithmic Coefficient Matrix for Centrally Symmetric Seven-Node Rational Configurations"
subtitle: "Research No. 81 — AI-audited proof-source preprint candidate"
author: "Ryutaro Yonezu"
date: "2026-11-22"
geometry: margin=24mm
fontsize: 10pt
mainfont: "Noto Serif"
monofont: "DejaVu Sans Mono"
colorlinks: true
---

**Research status:** General theorem: **independent AI mathematics audit PASS**, as reported in the Stage 06 addendum; six-configuration Windows exact finite check: **PASS (not a full theorem audit)**. **NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.**

**Editorial notice:** This is a collected proof-source edition. The five mathematical source documents below are reproduced verbatim, with no change to their mathematical statements, equations or proofs. Statements in the original dated source documents such as "PRIVATE / HOLD", "pending audit", and "no Windows test" record their *earlier drafting status*. The current audit status is given above; it does not imply human peer review or a separate mathematical audit of this typesetting.

**Provenance:** Frozen v0.7 SHA256 `ef40748e44e13280e00b4db496a3296119fa1adb2659afb869e5865f3765c6f4`. The original six-stage outer parent ZIP SHA256 `2cfcad697ae600b1f3f4ca9b925229d999d0384c0d3ea1c78d9b7fab50fe06ee` was recovered and directly SHA256-verified; the Stage 05 audit request ZIP SHA256 `a4317074478a5af590eda36bc66c3aee682e0ee64f013024d5805e52ea678419` was also recovered and verified. The original completion proof and certificate match those source archives byte-for-byte. The finite Windows check does not prove the general theorem. The optional single-GCD source is supporting historical material and is not needed in the final proof chain. See the accompanying reproducibility materials for the D=2 reduction and the supporting certificates.

# Main theorem and final completion argument



# Seven-node rational regularity via a seventh-power arithmetic progression
2026-11-20 JST — Research continuation, PRIVATE / HOLD.
NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.

## Statement and dependencies
The original D=2 logarithmic coefficient matrix A, with entries A[n,(i,j)] = b_i^(n-j)/(n-j) for n>j and zero otherwise (n=1,...,18; i=1,...,6; j=0,1,2), is nonsingular for the seven distinct nodes {0, ±a, ±b, ±c}, where a,b,c are positive distinct rationals. This is a proof proposal pending independent audit. Scaling by a nonzero rational lambda multiplies row n by lambda^n and column (i,j) by lambda^(-j), so denominators may be cleared and the gcd removed. Order 0<a<b<c and gcd(a,b,c)=1.

Dependencies: frozen v0.7 (SHA256 ef40748e44e13280e00b4db496a3296119fa1adb2659afb869e5865f3765c6f4), in particular its nested v0.5 necessary residue reduction; symmetric_D2_radius_proof.md; symmetric_seven_2adic_proof.md; symmetric_seven_small_prime_proof.md; Theorem 1 in symmetric_seven_global_proof.md. No reverse residue reduction is used. The preceding single-gcd case analysis is not needed. The cited theorem of Darmon and Merel is an external established theorem, not newly proved here.

## Proof
Suppose A singular. By the global factorization theorem, define d=gcd(b,c), e=gcd(a,c), f=gcd(a,b). Then there exist positive integers u,v,w,g and eps_a,eps_b,eps_c in {1,2}, exactly one 2, with

    a=e f u^2, b=d f v^2, c=d e w^2,
    c^2-b^2=g eps_a d^2 u^3,
    c^2-a^2=g eps_b e^2 v^3,
    b^2-a^2=g eps_c f^2 w^3.

The three square factors u,v,w have common gcd 1: any common prime would divide a,b,c. After dividing each difference by its shared factor squared,

    e^2 w^4-f^2 v^4=g eps_a u^3,
    d^2 w^4-f^2 u^4=g eps_b v^3,
    d^2 v^4-e^2 u^4=g eps_c w^3.

Multiply the first by u^4, the second by v^4, the third by w^4. The sum of the first and third left sides equals the second. Cancel positive g to obtain

    eps_a u^7 + eps_c w^7 = eps_b v^7.

Darmon–Merel, Main Theorem (1), states that X^n+Y^n=2 Z^n has no nontrivial primitive integer solution for n>=3, where trivial means XYZ=0 or ±1. The author-hosted manuscript dated 2001-01-05, pp. 1–2, was consulted directly (including page images); the journal article is J. reine angew. Math. 490 (1997), 81–100, DOI: 10.1515/crll.1997.490.81. URL: https://perso.imj-prg.fr/loic-merel/wp-content/uploads/merel-pub/winding.pdf .

If eps_a=2 then (X,Y,Z)=(v,-w,u); if eps_c=2 then (v,-u,w); if eps_b=2 then (u,w,v). Each triple is primitive and has nonzero product. The theorem forces u=v=w=1, because they are positive integers. The first two sign-mixed cases are then incompatible with the original seventh-power equality. Hence eps_b=2, eps_a=eps_c=1.

The divided square-difference equations now reduce to e^2-f^2=g and d^2-e^2=g. Put t=f^2>0 and h=g>0. Then the squared radii (X,Y,Z)=(a^2,b^2,c^2) are

    X=t(t+h), Y=t(t+2h), Z=(t+h)(t+2h).

No assumption about which shared factors are nontrivial is needed. In particular this remaining branch must be checked, rather than being dismissed as a trivial configuration: distinct radii are still possible before imposing the scalar equations.

For squared radii X_i in {X,Y,Z}, put

    g0=1/(-XYZ)^3,
    gi=1/[8 X_i^3 product_{j!=i}(X_i-X_j)^3],
    G=g0+2 sum_i gi,
    C=-sum_i gi (9+12 X_i sum_{j!=i}1/(X_i-X_j)).

The centered D=2 residue matrix M has det M=-(G+C)(3G+2C)/8. Set H=h^6 t^6(t+h)^6(t+2h)^6. Exact rational simplification yields

    G+C=3 F/(32 H),
    3G+2C=3 J/(4 H),

where

    F=84h^6+600h^5t+1396h^4t^2+1680h^3t^3+1150h^2t^4+438ht^5+73t^6,
    J=(11h^2+12ht+6t^2)(2h^4+12h^3t+18h^2t^2+12ht^3+3t^4).

All factors and coefficients are positive at t,h>0. Both rational identities are obtained by direct substitution into the scalar expressions and checked symbolically by symmetric_seven_completion_certificate.py. Thus det M<0 on this branch, contradicting singularity of A, which requires singularity of M. QED subject to the stated proof dependencies.

## Status and limits
This closes all shared-gcd patterns simultaneously, including the arithmetic-progression exceptional branch. It is an unbounded theorem proposal for the centrally symmetric seven-node D=2 family only. It does not settle arbitrary nonsymmetric seven-node configurations, nine-node symmetric configurations, arbitrary D or the original unrestricted rational conjecture. The new proof uses exact symbolic identities, no finite height cutoff, and depends on the external generalized Fermat theorem. It is not an independent audit. The frozen mathematical source is unchanged; no v0.8 freeze or Windows test; no publication permission. Novelty remains inconclusive. The primewise support proof and necessary residue reduction require review as part of the future independent audit.



\newpage

# Supporting source 1: symmetric\_seven\_2adic\_proof.md



# A 2-adic certificate for centrally symmetric seven-node configurations (D=2)
PRIVATE / HOLD — NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.

Dependencies: frozen v0.7 and `symmetric_D2_radius_proof.md` (necessary residue reduction and radius formulas). No inverse residue reduction is invoked. Normalize rational radii to primitive distinct positive integers a,b,c by scaling. This note is a computer-assisted proof proposal, not independently audited.

## Theorem
The original matrix is nonsingular if at least one primitive radius is even, or if all three are odd and the sorted 2-adic valuations of their squared differences are d,d,e with e>=d+2. Thus any singular rational seven-node centrally symmetric configuration must have three odd primitive radii with depths d,d,d+1, d>=3.

## Polynomial proof
Use X,Y,Z for the squared radii. With g0=(-XYZ)^(-3), gi=1/(8 Xi^3 product_{j!=i}(Xi-Xj)^3), set G=g0+2 sum gi and C=-sum gi(9+12 Xi sum_{j!=i}1/(Xi-Xj)). The previous reduction gives det M=-(G+C)(3G+2C)/8. Construct primitive integer numerator polynomials P1,P2 of G+C,3G+2C by exact cancellation over QQ, selecting signs so the coefficients of A^4 in Pi(1,A,0) are -5,-3 respectively. Each polynomial is symmetric, homogeneous of degree 12, and has 61 nonzero monomials. Denominators are nonzero for the allowed squared radii. Homogeneity allows division by any odd squared radius, which is a 2-adic unit.

For a term c_ij A^i B^j write W=i e+j f+v2(c_ij), where e=v2(A), f=v2(B). The companion script constructs the polynomials from the rational functions and verifies all stated strict weighted inequalities for all monomials. The verification is finite because W is affine in e,f; each unbounded cone is given as a base plus nonnegative combinations of generators, and strict positivity at the base plus nonnegative slopes suffices. It does not search just a bounded set of valuations.

* One odd radius, two even with unequal valuations: use (1,A,B), e>=2, f>=e+2. The unique lowest term is A^4 for both polynomials; valuations are 4e. Cone base (2,4), generators (1,1),(0,1).
* One odd radius, two even with equal valuations: use (1,A,A+B), e>=2, f>=e+3. The latter inequality follows since odd squares are 1 mod 8 after removing equal powers of 2. A^4 is uniquely lowest, with coefficient 8 or 4 respectively; valuations 4e+3 and 4e+2. Cone base (2,5), generators (1,1),(0,1).
* Two odd radii and one even: use (1,1+A,B), e>=3, f>=2 even. Only candidates for the least W are A^4 and B^3, with respective coefficients (-5,-8) for P1 and (-3,-4) for P2. Every other term has larger W than at least one candidate, checked at base (3,2) with coordinatewise nonnegative slopes. P1 has unequal candidate valuations 4e and 3f+3 by parity. For P2, the tie 4e=3f+2 occurs exactly at (e,f)=(5+3t,6+4t), t>=0. All other terms have W at least 4e+3, verified at t=0 with nonnegative slopes. For A=2^e u, B=2^f v^2 with u,v odd 2-adic units, the tied terms after division by 2^(4e) give -3u^4-v^6 = -4 mod 8 (odd square gives v^6=1 mod 8). So the sum has valuation exactly 4e+2, without vanishing.
* All odd radii: by the ultrametric inequality and the two-element residue field the three squared-difference depths are d,d,e with e>d, d>=3. Permute so the closest pair is (1,1+A), and use (1,1+A,1+B) with v2(A)=e,v2(B)=d. If e>=d+2, the unique lowest term is B^5, coefficient 8 for P1, 4 for P2. Cone base (5,3), generators (1,1),(1,0). Hence both polynomials are nonzero. This completes the claimed sufficient conditions.

## A genuine limitation of the method
Put (X,Y,Z)=(1,1+16u,9). The polynomial P1 divided by 2^18 and P2 divided by 2^17 are integer polynomials in u, each reducing to u+1 mod 2. By simple-root Hensel lifting each has its own root u in Z_2 with u odd. Then 1+16u is a nonzero 2-adic square (every unit congruent to 1 mod 8 is a square in Q_2). The squared radii are distinct since their difference depths are 3,3,4. Thus each scalar individually admits a genuine Q_2 zero in the unresolved regime; the roots need not coincide. Consequently the reduced determinant can vanish over Q_2. This alone does not prove singularity of the original matrix over Q_2, since the converse reduction was not invoked, and is not a rational counterexample.

## Finite checks and limitations
Run `symmetric_seven_2adic_certificate.py` beside `symmetric_D2_radius_certificate.py`, `d2_moment_reduction.py` and the frozen v0.7 ZIP. Requires Python/SymPy. All weighted inequalities and both Hensel polynomial reductions verified; lifts checked mod 2^17. Primitive triples with maximum radius <=50: 16648 total; new theorem covers 15418 (all checked by exact rational scalar evaluation); old radius witnesses for primes 5<=p<101 cover 16628; union 16643, of which 15 are newly covered. Remaining five verified by both frozen exact M and original integer-cleared determinant. Frozen SHA256 verified. No exhaustive rerun of previous certificates, no fresh literature search, no independent audit or Windows validation. No assertion for arbitrary radii in the unresolved regime or for arbitrary nonsymmetric seven-node configurations.



\newpage

# Supporting source 2: symmetric\_seven\_small\_prime\_proof.md



# Small-prime nonvanishing for centrally symmetric seven-node configurations (D=2)

PRIVATE / HOLD — NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.

## Scope and dependencies

This is a computer-assisted proof proposal extending `symmetric_D2_radius_proof.md` and `symmetric_seven_2adic_proof.md`. The frozen v0.7 necessary residue reduction is assumed; its converse is not needed. Normalize rational radii to distinct positive primitive integers a,b,c. Neither the frozen bundle nor previous certificates are modified. No independent audit or Windows validation.

## Theorem

For p=3 or p=5 the original D=2 matrix for nodes {0,±a,±b,±c} is nonsingular if at least one radius is divisible by p, or if the three p-adic valuations of squared-radius differences are not all equal.

Thus, using also the earlier 2-adic result, any singular rational configuration of this type must have all three primitive radii coprime to 30, squared difference depths d,d,d+1 at 2 (d>=3), and all three squared-difference depths equal at 3 and at 5. At 3, the common depth is >=1 because all nonzero squares are 1 modulo 3. At 5 the common depth is also >=1: three unit squares occupy at most two residue classes. These are necessary conditions, not a full nonsingularity theorem.

## Polynomial proof

Let X,Y,Z denote squared radii. Define g0=(-XYZ)^(-3), gi=(8 Xi^3 product_{j!=i}(Xi-Xj)^3)^(-1), G=g0+2 sum gi, C=-sum gi(9+12 Xi sum_{j!=i}1/(Xi-Xj)). The earlier radius identity gives det M=-(G+C)(3G+2C)/8. Take the primitive integer numerators P1,P2 of these two scalars, with signs fixed by the coefficients -5,-3 of A^4 in Pi(1,A,0). Both are symmetric homogeneous polynomials of degree 12 with 61 terms; denominators are nonzero on admissible radii. By homogeneity and symmetry normalize a unit squared radius to 1. All other coordinates remain p-adic squares. The companion certificate verifies strict weighted monomial comparisons on unbounded cones: if W(i,j)=ie+jf+v_p(c_ij), strict inequality at a base and nonnegative slope along each cone generator imply the inequality throughout the cone. The polynomial identities and comparisons below are reconstructed from the rational scalar expressions, not from a hard-coded list of coefficients.

### Two divisible radii

Use (1,A,B), e=v_p(A), f=v_p(B), both even and >=2. If unequal, arrange f>=e+2. The unique least-weight term is A^4 with coefficient -5 or -3 respectively (including its coefficient valuation). The certificate checks base (2,4) and rays (1,1),(0,1).

If e=f, divide A,B by p^e to get square units u,v. The homogeneous degree-four parts are

H1=-(A^2-3AB+B^2)(5A^2-2AB+5B^2),
H2=-(A^2-3AB+B^2)(3A^2-2AB+3B^2).

Every other term has degree >=5, hence valuation >=5e. For p=3 the unit squares both reduce to 1 and both H_i(u,v) are units. For p=5 and u=v mod 5 both are units. For p=5 and u!=v mod 5 the residues are 1,4 in some order. The second factor of each H_i is a unit and the first factor has valuation exactly one by

4(u^2-3uv+v^2)=(2u-3v)^2-5v^2,

since 2u-3v is divisible by 5. Thus the initial valuation is 4e or 4e+1, strictly less than 5e. Neither scalar numerator vanishes.

### One divisible radius

If the two unit squares agree modulo p, use (1,1+A,B), e=v_p(A)>=1, f=v_p(B)>=2 even. The only possible lowest terms are -5 A^4 and -8 B^3 for P1, or -3 A^4 and -4 B^3 for P2. The certificate compares each other term against at least one of these two on the cone e>=1,f>=2. If the coefficient of A^4 has valuation 1, equality of weights is impossible: 4e+1 is odd and 3f even. Otherwise, in case of a tie, the unit part after scaling equals -5u^4-8v^6 or -3u^4-4v^6, where u is an arbitrary unit and v is a unit square root of the unit part of B. Direct enumeration of the nonzero residues for p=3,5 in the cases with unit A^4 coefficient proves nonvanishing. If the two unit squares differ modulo p, necessarily p=5. Use (1,4+A,B). The constant coefficients -103680 and -62208 have valuations 1 and 0; the certificate verifies they are uniquely lowest for e>=1,f>=2.

### No divisible radii

For p=5 if two square classes occur, exactly one pair collides; the earlier mirror collision theorem applies (p>3). Otherwise all squares occupy one residue class (always the case at p=3). If pairwise difference depths are unequal, the ultrametric property gives d,d,e with e>d>=1. Choose the closest pair as (1,1+A), and the remaining square as 1+B, with v_p(A)=e and v_p(B)=d. The unique least-weight term in Pi(1,1+A,1+B) is B^5, with coefficient 8 or 4. The certificate verifies base (2,1) and rays (1,1),(1,0). Both coefficients are units for p=3,5. This completes the proof given the earlier necessary residue reduction.

## Verification and limitations

Run `symmetric_seven_small_prime_certificate.py` in the directory containing `symmetric_D2_radius_certificate.py`, `d2_moment_reduction.py` and the frozen v0.7 ZIP. Requires Python/SymPy. Both scalar polynomials passed all unbounded weighted cone and residue checks. For primitive positive triples with maximum radius <=50: 16648 total, p=3 covers 15236, p=5 covers 15526, their union covers 16546; all 16546 checked against exact rational scalar evaluations. The previous 2-adic and odd-prime witness conditions (primes 5<=p<101) cover 16643; all conditions together cover 16648. Previous five uncovered triples all covered by the new conditions. The original determinant was not re-evaluated for this full sample, nor was the previous weighted certificate rerun: old witness coverage is recalculated using its predicate. Frozen SHA256 verified. No novel claim about the unresolved primitive triples in general, nor about nonsymmetric nodes. No new literature search or independent audit.



\newpage

# Supporting source 3: symmetric\_seven\_global\_proof.md



# Global factorization obstruction for symmetric seven-node rational configurations (D=2)

PRIVATE / HOLD — NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.

## Scope and dependencies

Use the frozen v0.7 necessary residue reduction and the symmetric D=2 scalar formulas in `symmetric_D2_radius_proof.md`. Use the prior 2-adic and p=3,5 theorems in `symmetric_seven_2adic_proof.md` and `symmetric_seven_small_prime_proof.md`. Both corresponding certificates were replayed successfully this turn. The reduction's converse is not required. The frozen v0.7 ZIP is unmodified, SHA256 ef40748e44e13280e00b4db496a3296119fa1adb2659afb869e5865f3765c6f4. No independent audit or Windows test.

## Theorem 1 (global necessary factorization)

Let 0<a<b<c be primitive positive integer radii, obtained by clearing rational denominators and removing their common gcd. Suppose the original D=2 matrix at {0,±a,±b,±c} is singular. Set d_a=gcd(b,c), d_b=gcd(a,c), d_c=gcd(a,b). Then there are positive integers u_a,u_b,u_c such that

    a=d_b d_c u_a^2, b=d_a d_c u_b^2, c=d_a d_b u_c^2.

Let g=gcd(c^2-b^2,c^2-a^2,b^2-a^2). There are epsilon_a,epsilon_b,epsilon_c in {1,2}, exactly one equal to 2, such that

    c^2-b^2 = g epsilon_a d_a^2 u_a^3,
    c^2-a^2 = g epsilon_b d_b^2 u_b^3,
    b^2-a^2 = g epsilon_c d_c^2 u_c^3.

Furthermore gcd(g,abc)=1, and all radii are coprime to 30. These identities are necessary, not sufficient, for singularity.

### Proof

Let P_1,P_2 be the signed primitive numerators of G+C, 3G+2C from the preceding certificates. They are symmetric homogeneous integer polynomials in the squared radii. Singular A implies singular M, hence at least one P is zero. Fix such a P. Set (K,J)=(5,8) or (3,4), respectively. Direct symbolic reconstruction in the companion certificate proves the following identities/support facts:

1. P(1,Y,0)=-K Y^4(Y-1)^4; P(1,1,Z)=J Z^3(Z-1)^5.
2. P(1,1+A,B) has precisely the componentwise-minimal monomials -K A^4 and -J B^3. Every other monomial is strictly heavier than one of them for positive valuations of A,B at p>=7.
3. P(1,A,B) has no total degree below four, and its degree-four part is -(A^2-3AB+B^2)(K A^2-2AB+K B^2). At A=B=1 this part equals J. For unequal positive valuations of A,B, its least-weight term is the pure fourth power of the less-divisible variable, strictly below every other term, for p>=7.
4. In P(1,1+A,1+B), for e=v_p(A)>=f+1 where f=v_p(B)>=1, the term J B^5 is uniquely least-weight at all odd p for which J is a unit. Indeed every other exponent (i,j) satisfies i+j>=5 and 2i+j>5; hence ie+jf>5f.

These follow from the finite list of monomial exponents, with identities verified exactly in `symmetric_seven_global_certificate.py`. In each p-adic chart divide squared radii by a unit squared radius, using symmetry and homogeneity; none of the valuation comparisons changes when multiplying by such units. The normalized coordinates are p-adic integers.

At p=2 the preceding theorem forces odd radii and sorted difference depths d,d,d+1. At p=3,5 the preceding theorems force unit radii and equal difference depths. Thus these primes never divide a radius.

For any p>=7:

* If p divides no radius, the three difference depths must be equal. If just two squares collide modulo p, identity 1 on P(1,1,Z) excludes zero. If all three collide with unequal depths, choose the closest pair as (1,1+A) and the third square as 1+B; fact 4 excludes zero. If no pair collides all depths are zero.
* If p divides exactly one radius, say a, singularity forces b^2=c^2 mod p by identity 1 applied to P(1,Y,0). Choose b^2 as the unit normalizer. In P(1,1+A,B), v_p(A)=v_p(c^2-b^2)=e>0 and v_p(B)=2v_p(a)=f>0. Because p>=7 all leading coefficients are units. Fact 2 forces 4e=3f; otherwise there is a unique least-weight term. Consequently v_p(a) is even, say 2t, and v_p(c^2-b^2)=3t. The two differences involving a are units.
* If p divides exactly two radii, say b,c, primitivity makes a a unit. By fact 3, unequal squared valuations make P nonzero, so v_p(b)=v_p(c)=t>0. After unit normalization write A=p^{2t}U, B=p^{2t}V. If U=V modulo p the degree-four part equals J U^4 modulo p, which is nonzero; all terms of higher degree have strictly larger valuation. Consequently the two scaled squares differ modulo p, and v_p(c^2-b^2)=2t. The other differences are units.

No prime divides all three radii. The three gcds d_a,d_b,d_c are pairwise coprime; a shared prime has equal exponents in its two radii. All remaining prime powers of each radius have even exponents. This proves the displayed decomposition of the radii. By the primewise analysis, primes dividing abc never divide g. For odd primes not dividing abc the difference valuations are equal and exactly absorbed by g. At 2 exactly one difference has one extra factor 2. For a prime dividing a alone, its residual power in c^2-b^2 is the corresponding power of u_a^3; for a prime dividing b,c it is the corresponding power of d_a^2. All other differences are units in both cases. Permute the labels as needed. Unique factorization proves the three identities. QED.

## Theorem 2 (pairwise coprime radii)

If gcd(a,b)=gcd(a,c)=gcd(b,c)=1 after primitive integer normalization, the original D=2 matrix is nonsingular.

Proof. If singular, Theorem 1 gives a=u^2,b=v^2,c=w^2 with positive u<v<w. The additive identity among differences gives

    epsilon_b v^3 = epsilon_a u^3 + epsilon_c w^3.

Since w>v, epsilon_b must be 2; the other epsilons are 1. Thus v^3 is the midpoint of u^3 and w^3. The function t -> t^(4/3) is strictly convex for t>0, so w^4-v^4>v^4-u^4. On the other hand the original difference equations imply w^4-v^4=g u^3<g w^3=v^4-u^4. Contradiction. QED.

## Corollary (only the two smallest radii share prime factors)

Suppose gcd(a,c)=gcd(b,c)=1 but d_c=gcd(a,b)>1. The original matrix is also nonsingular. Otherwise a=d_c u^2,b=d_c v^2,c=w^2, hence u<v and w>sqrt(d_c)v. The necessary additive equation would give epsilon_b v^3=epsilon_a u^3+epsilon_c d_c^2 w^3. Its right side exceeds d_c^(7/2)v^3>2v^3, impossible. QED.

## Computations and limits

New companion certificate reconstructs both numerator polynomials, checks all local support identities, checks both exact rational scalars for 6106 pairwise coprime triples among 16648 primitive triples up to height 50, and screens all 24754 primitive triples with radii coprime to 30 up to height 200 against Theorem 1. No triple survives the necessary identities. Combined with the prior small-prime theorems this supplies a finite theorem for all primitive triples up to height 200, conditional on the stated proof dependencies; no new direct determinant checks were made for the entire sample. The earlier 2-adic and small-prime certificates were rerun, including their original residual five direct determinant checks. No conclusion for all triples sharing primes in the other patterns. Not a proof of unrestricted rational regularity. No new literature search, full old suite replay, independent audit, or Windows validation.



\newpage

# Supporting source 4: symmetric\_seven\_single\_gcd\_proof.md



# Elimination of single shared-gcd patterns in the symmetric seven-node D=2 problem
2026-11-20 JST — PRIVATE / HOLD
NOVELTY INCONCLUSIVE / REFERENCES PARTIAL / NOT HUMAN PEER REVIEWED / All rights reserved.

## Dependencies and status
Uses Theorem 1 of `symmetric_seven_global_proof.md` in the 2026-11-20 handoff. The 52 manifest entries and the frozen v0.7 archive SHA256 ef40748e44e13280e00b4db496a3296119fa1adb2659afb869e5865f3765c6f4 matched. The global, 2-adic, and small-prime certificates were replayed successfully in this session. No full v0.7 suite replay, independent audit or Windows run. No change to the frozen archive. These proposed proofs depend on the necessary residue reduction and radius formulas, not their converse.

Write d=d_a=gcd(b,c), e=d_b=gcd(a,c), f=d_c=gcd(a,b), and u=u_a,v=u_b,w=u_c. Assume singularity, so
    a=ef u^2, b=df v^2, c=de w^2,
    c^2-b^2=g eps_a d^2 u^3,
    c^2-a^2=g eps_b e^2 v^3,
    b^2-a^2=g eps_c f^2 w^3.
Exactly one epsilon is 2; all others 1. All radii are coprime to 30, hence each nontrivial gcd is >=7. Also a<b<c. Divide the additive relation by the positive common factor (def)^(-3/2) to obtain
    eps_b e^(7/2)b^(3/2)=eps_a d^(7/2)a^(3/2)+eps_c f^(7/2)c^(3/2).

## Proposition 1: if e=1, then f=1 is necessary for singularity
From the last equality, 2 b^(3/2)> f^(7/2)c^(3/2), so f^(7/2)<2. As f is a positive integer coprime to 30, f=1. This also excludes d>1,f>1,e=1, extending the earlier smallest-pair-only result.

## Proposition 2: d=f=1, e>1 is impossible
Then a=e u^2,b=v^2,c=e w^2, so u<w. The difference equations give c^2-b^2 <= 2(b^2-a^2), hence c^2<3b^2. But eps_b e^2 v^3=eps_a u^3+eps_c w^3<4w^3. Thus (b/c)^3=v^6/(e^3 w^6)<16/e^7<=16/7^7<1/27, so b/c<1/3, contradicting c^2<3b^2.

## Proposition 3: d>1, e=f=1 is impossible
Here a=u^2,b=d v^2,c=d w^2, with w>v. The additive equality forces eps_b=2, eps_a=eps_c=1. Then d^2 u^3=2v^3-w^3<v^3. Put X=(a/b)^2, t=w/v, Z=(c/b)^2=t^4. In particular 0<X<d^(-14/3)<1/2401. Dividing the first difference by the third produces
    (t^4-1)/(1-X)=(2-t^3)/t^3,
    t^7=2-X(2-t^3).
As 1<t^3<2, 2-X<t^7<2. Since (11/10)^7<2-1/2401 and (11/10)^4>7/5, we obtain 7/5<Z<2.

The two scalar numerator polynomials P1,P2 in squared radii are homogeneous, so a singular point would satisfy P_i(X,1,Z)=0 for at least one i. Reconstruct from the radius formulas. For each i the signed numerator is p0(Z)+X p1(Z)+X^2 p2(Z)+R(X,Z), where
    p0=-K Z^4(Z-1)^4;
    p1=L Z^3(Z-1)^4(Z+1);
    p2=-Z^2(Z-1)^4(H Z^2+I Z+H).
(K,L,H,I)=(5,17,16,53) or (3,11,12,37). All remaining powers of X are at least 3. On the rectangle 0<X<=1/2401, 7/5<=Z<=2, p1/|p0|<8 and p2<=0. Direct exact expansion yields a bound |R|<=M X^3, with M=sum_{i>=3,j}|c_ij|2^j=64184 or 44392. In particular
    P <= -K(7/5)^4(2/5)^4(1-8/2401)+M/2401^3 < 0.
Both final rational inequalities and the coefficient identities are checked by the new companion certificate. Thus neither numerator can vanish, contradiction. No finite radius bound is used in the proof.

## Proposition 4: an additional two-shared-gcd subcase
If d=1, e>1, f>1 and eps_a=2, no singularity is possible. Here v^2>e u^2 because a<b. Define S=(c^2-b^2)/(c^2-a^2)=2u^3/(e^2v^3). Then 0<S<2/e^(7/2). Also b^2/c^2=1-S(1-a^2/c^2)>1-S. The additive equality with eps_b=eps_c=1 gives f^2w^3=e^2v^3(1-S). Consequently
    (f/e)^7=(b/c)^3(1-S)^2>(1-S)^(7/2)>=1-(7/2)S>1-1/e.
The middle inequality is Bernoulli's inequality and the last uses e>=7. But (f/e)^7<1, so f<e and (f/e)^7<=(1-1/e)^7<=1-1/e, contradiction.

## Remaining cases
The earlier pairwise-coprime proof and Propositions 1–3 exclude all patterns with at most one nontrivial shared gcd, and the pattern d>1,f>1,e=1. Proposition 4 excludes part of d=1,e>1,f>1. Any singular triple must have e>1 and at least one of d,f>1. The remaining cases are d=1,e>1,f>1 with eps_a=1; d>1,e>1,f=1; and d,e,f>1. The complete rational seven-node theorem remains open in this work, as do the unrestricted rational problem and the novelty assessment. The new certificate checks exact polynomial identities and inequalities, not an independent audit. No claim of first discovery.



\newpage

# Publication integrity and limitations

This document is an assembled proof-source edition; the previously completed independent AI audit was performed on the source chain, not on this PDF's typeset text. The original parent ZIP and Stage 05 audit request ZIP have now been recovered; their SHA256 digests match the audit records. The completion proof and certificate are byte-identical across the recovered originals and the compiled source bundle. The four major proof sources in this edition match the parent ZIP byte-for-byte. The optional single-GCD source is supplementary historical work, not needed for the final theorem. A verified frozen v0.7 original is supplied as an immutable attachment.

The author has not yet authorized public GitHub/Zenodo release of this prepared candidate. DOI not assigned. All rights reserved.
