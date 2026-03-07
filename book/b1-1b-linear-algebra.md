# B1.1b Linear Algebra

> **SPDX-License-Identifier: CC0-1.0 (Text & Data) AND Apache-2.0 (Code)**
> The text and generated synthetic data in this chapter are licensed under the Creative Commons Zero (CC-0) Public Domain Dedication. All Python code snippets and scripts provided herein are licensed under the Apache-2.0 License.

## Glossary

* **NASA GCMD Keyword Viewer:** [https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all](https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all)
* **Wikipedia:** [https://www.wikipedia.org/](https://www.wikipedia.org/)
* **Wiktionary:** [https://www.wiktionary.org/](https://www.wiktionary.org/)
* **Affine Space:** A mathematical structure consisting of a set of points and a free and transitive action by a vector space. It lacks a true geometric origin.
* **Norm:** A mathematical function that assigns a strictly positive length or size to each vector in a vector space.
* **Linear Operator:** A mapping between vector spaces that preserves vector addition and scalar multiplication.
* **Matrix:** A rectangular array or table of numbers, symbols, or expressions.
* **Transpose:** An operator which flips a matrix over its diagonal.
* **Vector Space:** A collection of vectors, which may be added together and multiplied by scalars, and satisfying certain axioms.
# **Advanced Linear Algebra for Geodesy and Hydrographic Surveying: A Comprehensive Analysis of IHO S-5A B1.1b Standards**

## **1\. Introduction to Geodetic and Hydrographic Linear Algebra**

The rigorous positioning of spatial data in geodesy and hydrographic surveying is fundamentally reliant on the advanced principles of linear algebra. Modern surveying practice, characterized by the omnipresence of Global Navigation Satellite Systems (GNSS), Inertial Measurement Units (IMUs), and Multibeam Echosounders (MBES), requires the continuous translation, rotation, and scaling of coordinates across varying spatial reference frames.1 The International Hydrographic Organization (IHO) Category "A" standards (S-5A, Section B1.1b and related quantitative sections) mandate a profound theoretical and practical understanding of vector and affine spaces, linear operators, orthogonal projections, and spatial transformations.4 Category "A" programs introduce these competencies from the underlying mathematical principles level, empowering senior professionals to evaluate, derive, and implement robust georeferencing algorithms in scientific computing environments.3

This comprehensive report provides an exhaustive analysis of these mathematical foundations. It bridges pure algebraic theory with practical geomatics, detailing the derivations of two-dimensional (2D) and three-dimensional (3D) coordinate transformations, the critical role of matrix algebra in hydrographic sensor georeferencing, and the application of weighted inner products in least squares network adjustments.4 The mathematical models discussed herein form the invisible architecture that ensures satellite-derived geocentric coordinates can be accurately projected onto local topocentric datums, subsequently integrated with acoustic sounding data, and utilized to construct reliable nautical charts, digital elevation models, and standard seabed data models.8

## **2\. Foundational Spaces: Vector and Affine Geometries**

### **2.1 The Axiomatic Structure of Vector Spaces**

In classical linear algebra, a vector space ![][image1] over a field (such as the real numbers ![][image2] or complex numbers ![][image3]) is defined as a mathematical set equipped with two fundamental operations: vector addition and scalar multiplication.12 For a set to qualify as a vector space, these operations must satisfy a strict set of axioms, including closure, associativity, commutativity, and the existence of additive inverses and a distributive property.12

A defining and indispensable characteristic of any vector space is the mandatory existence of a unique origin, universally recognized as the null vector (![][image4]).13 The axiom dictates that for any vector ![][image5], the addition of the null vector yields the original vector: ![][image6].13 Consequently, within a vector space, the origin is a highly privileged and explicitly identifiable element. In geometric terms, every position vector is structurally tethered to this specific coordinate origin. A line within a vector space, defined by a direction vector ![][image7], is expressed as the set ![][image8] for all real scalars ![][image9]; notably, this foundational line must always pass precisely through the origin when ![][image10].13

### **2.2 Affine Spaces and the Absence of an Origin**

While vector spaces provide the mechanical framework for computational geometry, the physical reality of the Earth does not provide a naturally occurring, universally fixed origin. While geocentric reference systems mathematically designate the Earth's center of mass as a functional origin, this point is physically inaccessible, conceptually abstract, and its exact spatial location is subject to continuous geodetic refinement.14 Consequently, geodetic positioning frequently utilizes the mathematical concept of an *affine space* to represent terrestrial positions.13

An affine space ![][image11] can be rigorously conceptualized as a set of points equipped with a free and transitive action governed by an associated vector space ![][image1].16 In an affine space, points themselves cannot be meaningfully added together. More importantly, there is absolutely no privileged origin.13 The set ![][image11] does not distinguish any of its elements; mathematically, they are all entirely equivalent.13

Instead of adding points, the defining operation of an affine space involves the subtraction of two points ![][image12] to yield a displacement vector ![][image5], expressed algebraically as ![][image13].13 Conversely, adding a displacement vector ![][image7] to a given point ![][image14] actively translates it to a new spatial point ![][image15].16 The translation action ensures that for any point ![][image16], the operation ![][image17] yields the null vector ![][image4] of the associated vector space ![][image1].13

![][image18]

### **2.3 Practical Geodetic Implications of Affine Geometry**

This mathematical distinction is paramount in geodesy and surveying.15 When coordinate systems undergo translation (representing a shift in the mapping datum), the vectors representing distances or directions between two terrestrial points remain physically and mathematically invariant, but the position coordinates representing the affine points inherently change.14 A GNSS baseline, which measures the 3D displacement between two receivers, is a pure vector residing in the associated vector space ![][image1]. However, the calculated coordinates of the GNSS stations are affine points.

An affine transformation maps an affine space onto itself.17 This type of mathematical automorphism preserves the collinearity of points, ensuring that sets of parallel lines remain rigorously parallel post-transformation.17 It also preserves the ratios of distances along parallel line segments.17 However, it does not necessarily preserve the Euclidean origin, absolute distances, or angular relationships between intersecting lines.17 Every affine transformation can be functionally represented as the composition of a linear transformation acting upon the associated vector space and a spatial translation mapping the affine space.16 Consequently, while all purely linear transformations are affine, not all affine transformations are purely linear, as a linear transformation strictly preserves the origin, whereas an affine transformation permits the origin to drift.17

### Executable Example: Vector Space operations with SymPy

We can use SymPy to perform symbolic derivations of vector operations demonstrating closure and scalar multiplication.

```{code-cell} ipython3
import sympy as sp

u1, u2, u3 = sp.symbols("u1 u2 u3")
v1, v2, v3 = sp.symbols("v1 v2 v3")
c = sp.symbols("c")

u = sp.Matrix([u1, u2, u3])
v = sp.Matrix([v1, v2, v3])

addition = u + v
scalar_mult = c * u

print("Vector Addition:\n", addition)
print("\nScalar Multiplication:\n", scalar_mult)
```

## **3\. Inner Products, Norms, and Geodetic Weighting**

### **3.1 Euclidean Spaces and Orthogonality**

### Executable Example: Inner Product and Norm Calculation with NumPy

```{code-cell} ipython3
import numpy as np

def vector_add(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """Adds two vectors in a vector space."""
    return v1 + v2

def calculate_inner_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """Calculates the Euclidean inner product (dot product) of two vectors."""
    return float(np.dot(v1, v2))

def calculate_norm(v: np.ndarray) -> float:
    """Calculates the Euclidean norm (magnitude) of a vector."""
    return float(np.linalg.norm(v))

# Geodetic synthetic example:
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Inner product:", calculate_inner_product(v1, v2))
print("Norm of v1:", calculate_norm(v1))
```


Within a real vector space, the formal introduction of an inner product operation, denoted as ![][image19], algebraically induces a highly structured geometric environment, transforming the space into an inner product space or a Euclidean space.12 This structure facilitates the definition of absolute lengths and angular measurements. The standard Euclidean norm of a vector ![][image20], which represents its geometric magnitude, is defined as the square root of the inner product of the vector with itself: ![][image21].18

Two independent vectors are geometrically defined as orthogonal if their computed inner product is identically zero: ![][image22].18 The principle of orthogonality leads directly to the formulation of the Pythagorean Law in ![][image23]\-dimensional space, which asserts that for any orthogonal set of vectors, the squared norm of their sum equals the sum of their squared norms: ![][image24].18 This is an indispensable property utilized extensively in establishing orthogonal coordinate reference frames, such as the topocentric Local Level Frame (North, East, Down or East, North, Up) used in hydrographic vessel orientation.11

### **3.2 Weighted Inner Products in Adjustment Computations**

In classical, abstract linear algebra, the inner product is typically assumed to be uniform across all dimensions.12 However, in empirical geodetic adjustment computations, observations—such as measurements of terrestrial distances, angles, or satellite-derived GNSS baselines—possess highly varying degrees of statistical precision and physical reliability.7 To mathematically account for this inevitable observational disparity, geodesy continuously employs a *weighted* inner product.7

When adjusting an overdetermined geodetic network, the primary mathematical objective is to calculate an optimized solution that strictly minimizes the sum of the squares of the measurement residuals.21 Let the vector ![][image7] denote the measurement residuals, mathematically defined as ![][image25], where ![][image26] represents the raw observed values and ![][image27] denotes the theoretically adjusted values derived from the functional model.23 The least squares criterion fundamentally minimizes the weighted norm, expressed algebraically as the following quadratic form:

![][image28]  
where the square matrix ![][image29] functions as the indispensable weight matrix corresponding to the network observations.7

### **3.3 Stochastic Modeling and Variance Components**

The weight matrix ![][image29] is not arbitrarily assigned; it is rigorously defined as the mathematical inverse of the cofactor matrix ![][image30].7 The cofactor matrix is proportionally related to the formal variance-covariance matrix ![][image31] of the geodetic observations via the equation: ![][image32], where the scalar ![][image33] represents the a priori variance of unit weight.7

This advanced statistical approach mathematically transforms the isotropic Euclidean space into an anisotropic, non-uniform metric space. For example, in a traditional differential leveling network covering a total distance ![][image34], the formal variance of an observed height difference progressively increases as a function of the traversed distance.7 Consequently, the statistical weight assigned to a specific leveling run is intentionally configured to be inversely proportional to its total length (![][image35]).7

Similarly, for horizontal directions averaged across multiple rounds of measurement, the variance of the mean value decreases as the number of independent rounds (![][image23]) increases.7 The corresponding weight is therefore directly proportional to the number of rounds (![][image36]).7 The mathematical minimization of the weighted norm ![][image37] effectively ensures that highly precise, heavily weighted measurements exert a dominant geometric pull on the final adjusted coordinate positions, while less reliable observations are statistically suppressed.7

## **4\. Linear Operators and Matrix Algebra**

### **4.1 Linear Transformations and Matrix Representations**

A linear operator is a specialized mapping ![][image38] between two vector spaces that rigorously preserves the algebraic operations of vector addition and scalar multiplication.25 Specifically, for any vectors ![][image39] and any scalar ![][image40], the operator must satisfy ![][image41] and ![][image42].26 When the transformation maps a vector space strictly into itself (![][image43]), it is formally termed an endomorphism.26

In finite-dimensional vector spaces, such as the 3D spatial frames utilized in hydrography, every linear operator can be uniquely encoded and represented by a matrix with respect to a explicitly chosen basis.16 Matrix multiplication serves as the computational execution of the composition of linear mappings. The efficiency of converting complex spatial geometries into matrix notation allows geodesists to leverage automated scientific computing environments to perform rapid, high-volume coordinate transformations and coordinate system definitions.4

### **4.2 The Transpose and Orthogonal Matrices**

### Executable Example: Linear Operators and Matrix Operations

```{code-cell} ipython3
import numpy as np

def matrix_compose(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Composes two matrices (matrix multiplication)."""
    return A @ B

def matrix_transpose(A: np.ndarray) -> np.ndarray:
    """Returns the transpose of a matrix."""
    return A.T

def linear_operator_demo():
    """Demonstrates a simple linear operator applying to a vector."""
    A = np.array([[1, 2], [3, 4]])
    v = np.array([1, 2])
    return A, v, A @ v

# Geodetic synthetic example:
A = np.array([[0, -1], [1, 0]]) # 90 degree rotation
v = np.array([1, 0]) # Point on x-axis

print("Transformed vector v:", matrix_compose(A, v))
print("Transpose of A:\n", matrix_transpose(A))
```


The transpose of a matrix ![][image44], algebraically denoted as ![][image45], is formed by systematically interchanging its rows and columns.4 In the specific context of spatial transformations, orthogonal matrices play an unequivocally dominant role.28 An orthogonal matrix ![][image46] acts as a linear transformation that meticulously preserves inner products.19 Because the inner product dictates both length and angle, an orthogonal transformation operates as a rigid-body motion, preserving the exact geometry of the transformed spatial objects.19

By mathematical definition, the column vectors and row vectors of an orthogonal matrix constitute an orthonormal basis, resulting in the foundational matrix property:

![][image47]  
where ![][image48] represents the standard identity matrix.19 This property possesses profound computational implications: the inverse of an orthogonal matrix is mathematically identical to its transpose (![][image49]).19 In practical geodetic software, this structural property drastically simplifies the computational inversion of massive datum transformation arrays, bypassing computationally expensive matrix inversion algorithms in favor of a trivial transposition.19

### **4.3 Matrix Inversion and Condition Numbers**

While orthogonal matrices represent idealized rotations, broader geodetic problems—such as the least squares resolution of complex transformation parameters—often produce non-orthogonal coefficient matrices that require formal mathematical inversion.4 Solving systems of linear equations via numerical methods, such as Gaussian elimination, LU factorization, or Cholesky decomposition, requires a robust understanding of numerical stability.4

The numerical condition number of a matrix determines the theoretical bound on how sensitive the solution of a linear system is to small perturbations or inherent measurement errors in the input data.4 In surveying network adjustments, a matrix with a very high condition number is deemed "ill-conditioned," indicating that minor observational noise in the GNSS or total station measurements could cascade into massive, catastrophic errors in the calculated coordinates.4 Evaluating the condition number acts as a crucial quality-assurance mechanism within hydrographic data processing environments, preventing the validation of geometrically weak or rank-deficient survey networks.4

## **5\. Rotations, Translations, and Sensor Georeferencing**

### **5.1 The Special Orthogonal Group SO(3)**

Rotations in three-dimensional space constitute a highly specific class of linear operators. An orthogonal matrix ![][image46] represents a proper, physically realizable spatial rotation if and only if its determinant is exactly ![][image50] (![][image51]).29 Conversely, improper rotations exhibit a determinant of ![][image52] and imply a spatial reflection, which cannot be achieved by continuous physical motion.29

The continuous set of all proper 3D rotation matrices forms a rigorous algebraic structure known as the Special Orthogonal Group, denoted mathematically as ![][image53].29 A critical property of ![][image53] is that it is non-abelian, meaning the group operation (matrix multiplication) is non-commutative.29 Consequently, the sequence in which multiple spatial rotations are applied fundamentally alters the final geometric orientation.29 A quarter turn around the longitudinal ![][image54]\-axis followed by a quarter turn around the transverse ![][image55]\-axis yields an entirely different final attitude than applying the ![][image55]\-axis rotation first.29

### **5.2 Euler Angles vs. Dual Quaternions**

A generalized 3D rotation matrix is traditionally constructed through the sequential composition of three elemental rotations around the primary Cartesian axes (![][image54], ![][image55], and ![][image56]).19 Let the elemental rotation angles be denoted as ![][image57] (around ![][image54]), ![][image58] (around ![][image55]), and ![][image59] (around ![][image56]). The elemental rotation matrices are formally defined as:

![][image60]  
![][image61]  
![][image62]  
The complete spatial rotation matrix ![][image46] is the concatenated product of these elemental matrices: ![][image63].19

However, representing 3D spatial rotations using three sequential Euler angles introduces notorious mathematical vulnerabilities, primarily the phenomenon of gimbal lock, which manifests as unavoidable matrix singularities when specific rotation angles approach ![][image64].1 To circumvent these computational singularities in advanced 3D coordinate transformations, modern surveying algorithms increasingly employ quaternions and dual quaternions.1 Dual quaternions concisely encapsulate both 3D rotation and 3D translation into a single unified algebraic state, providing a robust, singularity-free iterative framework for executing symmetric similarity 3D coordinate transformations, such as transitioning between historical local datums and the World Geodetic System 1984 (WGS84).1

### **5.3 Marine Sensor Composition: Roll, Pitch, and Yaw**

The precise composition of rotation matrices is a ubiquitous operational necessity in hydrographic surveying, specifically during the georeferencing of Multibeam Echo Sounder (MBES) data via an Inertial Measurement Unit (IMU).2 High-end inertial navigation systems, such as the Applanix POS MV, continuously measure the dynamic attitude of the survey vessel with extraordinary precision, expressing this orientation via aeronautical Euler angles: Roll (![][image65]), Pitch (![][image66]), and Yaw (![][image58]).2

These marine orientation parameters directly map to linear algebraic rotation matrices about the vessel's locally defined orthogonal axes 20:

* **Roll (![][image65])**: A rotation about the vessel's longitudinal ![][image54]\-axis. Represented mathematically by ![][image67].33  
* **Pitch (![][image66])**: A rotation about the vessel's transverse ![][image55]\-axis. Represented mathematically by ![][image68].33  
* **Yaw (![][image58])**: A rotation about the vertical ![][image56]\-axis. Represented mathematically by ![][image69].33

To accurately map a raw depth sounding generated by a hull-mounted acoustic transducer into a global reference frame, the position vector of the sounding must undergo a rigorous sequence of matrix multiplications.3 The composite rotation matrix aligning the vessel frame (![][image70]) is algebraically constructed as:

![][image71]  
This composite matrix operator actively rotates the sounding from the vessel's dynamic local coordinate system into strict alignment with a stabilized local level frame (typically North, East, Down), fully compensating for the erratic rotational motion of the vessel over the seafloor.34

### **5.4 Lever Arms and Spatial Translations**

Beyond pure rotations, the georeferencing model relies heavily on spatial translations.6 A survey vessel hosts a constellation of disparate sensors—GNSS antennas, IMU origin points, and MBES transducers—each physically separated by fixed offsets known as lever arms.6 These static translational offsets must be rigorously surveyed (often relative to a primary granite block reference point defining the vessel frame) and added to the rotated vector equations to achieve absolute spatial positioning.3 A failure to properly compose these translation vectors with the IMU-derived rotation matrices, or applying them in an erroneous mathematical sequence, precipitates severe systemic artifacts in the final bathymetric BASE surface.3

## **6\. Orthogonal Projections**

### **6.1 Idempotent Matrices and Projection Operators**

In the realm of functional analysis and linear algebra, a projection is formally defined as a linear transformation ![][image29] from a given vector space to itself that exhibits idempotency.26 Mathematically, this mandates that ![][image72], or in matrix notation, ![][image73].26 This geometric property implies that applying the projection operator twice to any arbitrary vector yields the exact same spatial result as if it were applied merely once; the operation leaves its own projected image entirely unchanged.26

An *orthogonal* projection is a highly specialized variant that maps an arbitrary vector ![][image20] directly onto a designated subspace ![][image74], such that the resulting projected vector ![][image75] constitutes the absolutely closest point located within ![][image74] relative to the original vector ![][image76].36

According to the Orthogonal Decomposition Theorem, any spatial vector ![][image76] can be additively decomposed into ![][image77], where ![][image75] resides within the subspace ![][image74], and ![][image78] resides exclusively within the orthogonal complement of ![][image74].36 Crucially, this dictates that the error vector (or spatial difference vector), calculated as ![][image79], is strictly orthogonal to all possible vectors contained within the subspace ![][image74].36

If the subspace ![][image74] represents the specific column space of a matrix ![][image80] (where the independent columns of ![][image80] serve as base vectors for ![][image74]), the optimal projection ![][image75] is formulated algebraically by stating ![][image81] for some unknown coefficient vector ![][image82].36 Because the residual spatial vector ![][image83] must be mathematically orthogonal to the entire column space of ![][image80], it is compelled to reside within the null space of the transposed matrix ![][image84]. This geometric constraint seamlessly establishes the normal equation:

![][image85]  
Analytically solving this equation for the coefficient vector ![][image82] yields ![][image86].36 Substituting this result back confirms that the standard closed-form matrix formulation for the orthogonal projection operator ![][image29] onto the subspace ![][image74] is strictly derived as:

![][image87]  
Applying this specific matrix operator to any generic vector ![][image76] instantly returns its precise orthogonal projection ![][image88].36

### **6.2 Projecting Coordinates onto a Plane**

In the applied discipline of geomatics, the mathematical requirement to project a 3D coordinate onto a rigidly defined surface is a constant routine. The most fundamental projection scenario involves mapping a 3D topographic point onto an arbitrary 2D datum plane.37 When projecting a spatial point ![][image89] onto a specified plane mathematically defined by a normal vector ![][image90], the geometric projection establishes an intersecting line that penetrates the plane at exactly a 90-degree right angle.37

### **6.3 Ellipsoidal Projections in Geographic Information Systems**

A vastly more algebraically complex, yet practically essential, projection utilized in surveying involves the orthogonal projection of a 3D spatial point onto a biaxial or triaxial reference ellipsoid (e.g., the WGS84 ellipsoid).31 Because the Earth is technically an oblate spheroid rather than a uniform sphere or flat plane, the orientation of the normal vector relative to the ellipsoid's curved surface changes continuously depending upon the specific latitude.41

The orthogonal projection rigorously maps a geocentric Cartesian coordinate ![][image91] to its corresponding geodetic latitude, geodetic longitude, and ellipsoidal height ![][image92]. It accomplishes this by iteratively searching for the precise point located on the continuous ellipsoid surface where the surface normal line passes perfectly and orthogonally through the original ![][image91] point.40 This advanced geometric transformation effectively minimizes the algebraic distance function calculated between the spatial point and the quadratic surface equation of the reference ellipsoid, necessitating iterative numerical routines like Newton-Raphson to achieve millimeter-level closure.31

## **7\. Mathematical Derivation of Coordinate Transformations**

When synthesizing and integrating multiple spatial data sets—a cornerstone of Geographic Information Systems (GIS)—hydrographic surveyors must possess the mathematical capacity to transform coordinates seamlessly between varying geodetic reference frames (e.g., passing dynamically from a global ITRF satellite epoch directly to a local, historically defined national datum).43 The primary mathematical algorithms deployed for this integration are Similitudes (Similarity/Conformal Transformations) and Affine Transformations.11

### **7.1 Similitudes Versus Affine Mappings**

Table 1 outlines the fundamental mathematical distinctions between the primary transformation models utilized in contemporary geomatics.

| Transformation Model | Parameters (2D/3D) | Geometric Properties Preserved | Scale Factor Application | Primary Geodetic Use Case |
| :---- | :---- | :---- | :---- | :---- |
| **Conformal / Similarity** | 4 / 7 | True shape, spatial angles | Uniform globally (![][image93]) | Standard datum shifts (e.g., ITRF to WGS84) 11 |
| **Orthogonal** | 3 / 6 | Shape, angles, absolute distances | Fixed to Unity (1.0) | Rigid body translation and pure rotation 11 |
| **Affine** | 6 / 12 | Parallelism of lines | Differential (![][image94] scale differently) | Correcting local grid skew, legacy mapping integration 11 |
| **Polynomial** | Variable | None (Highly flexible distortion) | Non-linear functions | Warping historically distorted localized networks 19 |

A similarity transformation (frequently referred to as a conformal or Helmert transformation) rigorously acts to preserve the internal shape of a geometric figure and the exact angles located between intersecting lines.11 It mathematically accomplishes this stabilization by utilizing a strictly *uniform* scale factor ![][image93] applied identically in all spatial directions.11 In 3D space, defining this transformation requires 7 independent parameters: three spatial translations, three Euler rotation angles, and one overall scale factor.11 If the transformation's scale factor is mandated to be strictly ![][image95], the mathematical model reduces to a pure orthogonal transformation (rigid body motion), which flawlessly preserves absolute distance measurements.11

Conversely, the affine mathematical model provides a considerably higher degree of algebraic flexibility. It strictly preserves the geometric parallelism of lines but allows for differential scaling factors and axis skew (non-perpendicularity).11 Consequently, under an affine mapping, the inherent shape of a geographical object may be systematically stretched or sheared. In a pure affine transformation, the applied scale factor is highly dependent upon the spatial orientation.11 A full 3D affine transformation utilizes up to 12 parameters (three translations, three rotations, three entirely disparate scale factors exclusively for ![][image96], and three distinct 3D skew parameters).11 Affine models are frequently employed out of necessity when a localized legacy grid visibly exhibits systematic distortions, non-orthogonality, or glaring scale discrepancies directly between the surveyed Easting and Northing axes.11

### **7.2 Derivation of the 2D Conformal Transformation**

The two-dimensional conformal transformation, historically pioneered by the mathematician C.F. Gauss, elegantly relies on complex variables to continuously project an ellipsoid surface onto a flat map plane while strictly preserving angular integrity.19 A transformation transitioning from an arbitrary ![][image97] grid system directly to a formalized East-North (![][image98]) target system can be mathematically expressed as a generalized complex function ![][image99].19 For this spatial mapping to remain mathematically conformal, the underlying function must be purely analytic and rigorously satisfy the stringent Cauchy-Riemann equations:

![][image100]  
Expanding this analytic complex function specifically as a first-order polynomial explicitly yields ![][image101].19 By meticulously separating the real variables from the imaginary components, this complex equation produces two highly applicable linear equations:

* ![][image102]  
* ![][image103]

In these structural equations, the coefficients ![][image104] and ![][image105] operate directly as the Cartesian translation parameters (![][image106]).19 The multiplier coefficients ![][image107] and ![][image108] ingeniously encode both the required rotation angle (![][image109]) and the critical uniform scale factor (![][image93]) simultaneously, such that ![][image110] and ![][image111].19

Re-arranging these algebraic results into classic matrix notation, the 2D Conformal (often termed Helmert) transformation is universally expressed as:

![][image112]  
This highly efficient 4-parameter mathematical model (![][image113]) necessitates a minimum of two identical geodetic control points (providing four total observation equations) with coordinates precisely known in both reference systems to achieve a mathematical resolution.42

### **7.3 Derivation of the 2D Affine Transformation**

In operational scenarios where the source ![][image54] and ![][image55] surveying axes exhibit documented non-orthogonality or possess distinctly disparate metric scale disparities, the conformal model fails, and a 6-parameter 2D affine transformation must be mathematically derived.46 The corresponding observation equations are constructed using a generalized algebraic form without the Cauchy-Riemann constraints:

* ![][image114]  
* ![][image115]

In this expanded format, the constants ![][image104] and ![][image105] continue to function as positional translations.46 However, the remaining four coefficients ![][image116] operate entirely independently. Together, they possess the algebraic capacity to absorb two distinct axial scale factors, a generalized grid rotation angle, and a highly critical axis non-perpendicularity (shear/skew) parameter.46 Because this robust model incorporates 6 discrete mathematical unknowns, a minimum of three identical, non-collinear control points is strictly required to execute a valid solution.47

### **7.4 Derivation of the 3D Helmert Transformation**

The absolute global standard for 3D coordinate transformation in high-precision geodesy is the 7-parameter 3D Helmert (or similarity) transformation, which is most widely implemented across the industry via the Bursa-Wolf mathematical model.11 It comprehensively relates an initial source global geocentric reference frame (![][image117]) directly to a newly defined target frame (![][image118]) through the combined application of three dimensional translations (![][image119]), a single unified scale factor correction (![][image120], universally expressed in minute parts-per-million), and three independent spatial rotation angles (![][image121]).11

The rigorous, non-linear mathematical structure of the Bursa-Wolf equation is explicitly formulated as:

![][image122]  
To unequivocally prove the geometric conformality of this 3D spatial model, a mathematician must definitively establish that geometric angles are preserved intact within the 3D space.19 Given two arbitrary position vectors ![][image123] and ![][image7], the initial spatial angle ![][image66] between them is calculated using the standard inner product formulation: ![][image124].19

Applying the similarity transformation to these vectors (while ignoring translation, which does not alter angles), the newly transformed vectors become ![][image125] and ![][image126], where ![][image127].19 Calculating the updated inner product of these transformed vectors yields:

![][image128]  
Because the formulated rotation matrix ![][image46] is perfectly and rigorously orthogonal by definition (![][image129]), the complex equation elegantly reduces to ![][image130].19 Because the scalar lengths in the denominator of the cosine equation also scale uniformly by the factor ![][image93], the scale parameter perfectly cancels out mathematically, conclusively proving that ![][image131]. Therefore, the 3D Helmert transformation mathematically guarantees the preservation of all 3D spatial angles, rendering it a true conformal model.11

## **8\. Computing Transformations and Datum Conventions**

While the transformation equations detailed above are theoretically exact within an abstract vector space, in practical application, the surveyed coordinates of the common control points bridging the reference systems contain inherent, unavoidable observational errors.7 Therefore, the required transformation parameters (whether 4, 6, or 7\) are almost never solved purely algebraically; instead, they are stochastically estimated using a statistically redundant array of tie points via the Method of Least Squares.11

### **8.1 Linearization and the Gauss-Markov Model**

The computational process mandates the linearization of the heavily non-linear 3D transformation equations, utilizing a Taylor series expansion to architect a functional Gauss-Markov model.7 The resulting linearized observation equation assumes the classic matrix form:

![][image132]  
Within this highly structured algebraic architecture:

* ![][image133] is the primary observation vector. It consists of the metric coordinate differences identified between the targeted system points and the approximate points projected forward from the source system.7  
* ![][image80] serves as the critical design matrix (functionally the Jacobian matrix). It is populated with the precise partial derivatives of the transformation equations formulated with respect to each of the distinct unknown parameters.11  
* ![][image76] acts as the required vector of unknown parameter corrections that the algorithm must solve for (e.g., ![][image134]).11  
* ![][image7] represents the residual error vector encapsulating the random measurement noise inherent in the surveyed coordinates.11

### **8.2 Position Vector vs. Coordinate Frame Conventions**

A remarkably critical mathematical nuance—one that frequently and notoriously causes catastrophic positioning errors in hydrographic survey georeferencing—is the simultaneous existence of two competing, yet equally valid, 7-parameter coordinate conventions: the **Position Vector** rotation convention and the **Coordinate Frame** rotation convention (standardized by EPSG Operation Methods 1037 and 1032, respectively).54

Both of these computational models actively utilize a linearized, small-angle approximation of the rotation matrix ![][image46], a simplification that remains mathematically valid (to sub-millimeter precision) provided the required rotation angles are less than 10 arc-seconds.57 By applying standard Taylor series approximations (![][image135] and ![][image136] when utilizing radians), the complex multiplication of elemental rotation matrices simplifies drastically, intentionally disregarding negligible second-order angular products.57

The fundamental divergence between the two models occurs strictly in the philosophically assumed direction of the geometric rotation:

1. **Coordinate Frame Rotation (EPSG 1032\)**: This mathematical convention assumes that the *coordinate axes themselves* are physically rotated, while the position point vector remains entirely fixed in space.55 The linearized rotation matrix ![][image137] is constructed as:  
   ![][image138]  
2. **Position Vector Transformation (EPSG 1037\)**: Conversely, this convention assumes that the *point vector itself* is actively rotated within a strictly fixed and rigid coordinate frame.54 The corresponding linearized matrix ![][image139] is the exact mathematical transpose of ![][image137]:  
   ![][image140]

Consequently, to achieve the exact identical coordinate spatial output utilizing both conventions, a surveyor must manually flip the algebraic signs of the three rotation parameters (![][image121]).55 Failure to respect and identify the correct mathematical convention matrix programmed into the software leads to disastrous inverse rotations, misaligning geodetic networks and hydrographic depth surfaces by potentially hundreds of meters.42

### **8.3 Numerical Applications and Residual Analysis**

Because the 3D rotation matrix natively involves complex trigonometric functions governing the unknown rotation angles, the transformation is fundamentally non-linear.11 Therefore, the Gauss-Markov least squares solution cannot be solved in a single algebraic step; it must be processed iteratively.11

The critical vector of parameter updates ![][image76] is computed using the formulated normal equation, integrating the statistical weight matrix ![][image29]:

![][image141]  
Here, the matrix product ![][image142] generates a symmetric, positive-definite matrix that fully encapsulates the normal equations of the survey network.7 The ultimate mathematical inversion of this specific matrix—a process guaranteed by its positive-definite nature provided the column vectors of the design matrix ![][image80] remain linearly independent—yields the highly critical variance-covariance matrix of the estimated parameters.7

In a highly documented numerical test explicitly designed to transform global SWEREF 93 geocentric coordinates to the historical Swedish RT90/RH70 national datum (utilizing 12 surveyed common control points), the initial approximate parameters (scale ![][image143], rotations ![][image144], translations ![][image144]) were iteratively and sequentially updated.11 Over successive algebraic iterations, the update vector ![][image76] progressively approaches zero. The final convergence iteration successfully yielded an ![][image54]\-translation of ![][image145], a ![][image55]\-translation of ![][image146], and a ![][image56]\-translation of ![][image147], alongside highly precise micro-radian rotation parameters.11

![][image148]

Upon successfully determining the definitive mathematical transformation parameters, the residual errors (![][image7]) corresponding to every individual control point are strictly calculated by projecting the known coordinates back through the solved mathematical model.11 Geodetic best practices rigidly dictate evaluating these residuals not in the abstract geocentric ![][image149] frame, but by transforming the geocentric residual vectors into a locally oriented topocentric (North, East, Up) matrix orientation.11 This rotational translation renders the residuals geographically interpretable, allowing surveyors to visualize localized datum distortions.11

Extensive numerical investigation confirms that applying uniform weighting to 3D coordinate observations in these adjustments is highly sub-optimal.11 GNSS-derived ellipsoidal heights intrinsically exhibit significantly lower precision (higher variance) than horizontal positional data.11 By selectively adjusting the diagonal elements of the observation weight matrix ![][image29]—specifically, actively increasing the a priori variance assigned to the vertical 'Up' components—the least squares algorithm intentionally applies less statistical tension to the inherently weak vertical geometry.11 This optimal weighting model actively forces the regression matrix to prioritize the minimization of horizontal coordinate residuals, frequently resulting in dramatically superior planar transformation accuracy without corrupting the overarching mathematical integrity of the 3D transformation matrix.11

## **9\. Conclusion**

The rigorous implementation of advanced linear algebra is entirely non-negotiable for the successful execution of high-precision geodetic and hydrographic operations governed by the IHO S-5A standards. The abstract algebraic distinction between vector spaces and affine spaces forms the conceptual and theoretical bedrock, actively preventing mathematical absurdities when shifting mapping datums that lack absolute, physically defined origins. The precise application of inner products and highly structured orthogonal projections enables the seamless mapping of 3D spatial points onto complex mathematical reference ellipsoids, while weighted quadratic norms explicitly facilitate the optimal statistical least squares adjustment of overdetermined geodetic networks.

Furthermore, the integrity of all marine spatial data hinges entirely on the structurally correct implementation of matrix algebra. Whether computing a 6-parameter 2D affine map adjustment to reconcile legacy cartography, constructing a 7-parameter 3D Helmert transformation via the robust Bursa-Wolf model, or sequentially multiplying high-frequency roll, pitch, and yaw matrices to successfully compensate for extreme dynamic vessel motion over the seabed, the operator must meticulously adhere to established mathematical conventions. An intimate, theoretically grounded understanding of these linear algebraic operators directly and unequivocally dictates the metric accuracy, statistical reliability, and ultimate navigational safety of the resulting geospatial maritime products.

#### **Works cited**

1. Implementation of the dual quaternion algorithm for 3D similarity-based coordinate transformation between Ghana's local geodet, accessed March 6, 2026, [https://rgg.edu.pl/pdf-196448-119486?filename=Implementation-of-the-dua.pdf](https://rgg.edu.pl/pdf-196448-119486?filename=Implementation-of-the-dua.pdf)  
2. Hydrographic survey and mapping \- Applanix, accessed March 6, 2026, [https://applanix.trimble.com/en/industry/hydrographic-survey](https://applanix.trimble.com/en/industry/hydrographic-survey)  
3. Hydrographic Surveying \- USACE Publications, accessed March 6, 2026, [https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM\_1110-2-1003.pdf](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1003.pdf)  
4. STANDARDS OF COMPETENCE FOR CATEGORY "A ... \- IHO, accessed March 6, 2026, [https://iho.int/iho\_pubs/standard/S-5/S-5A\_Ed1.0.2.pdf](https://iho.int/iho_pubs/standard/S-5/S-5A_Ed1.0.2.pdf)  
5. Standards of Competence for Category "A" Hydrographic Surveyors (Preview PR) \- GitHub Pages, accessed March 6, 2026, [https://metanorma.github.io/mn-samples-iho/documents/s5a/document.pdf](https://metanorma.github.io/mn-samples-iho/documents/s5a/document.pdf)  
6. Field Procedures Manual \- NOAA Nautical Charts, accessed March 6, 2026, [https://nauticalcharts.noaa.gov/publications/docs/standards-and-requirements/fpm/field\_procedures\_manual\_2020.pdf](https://nauticalcharts.noaa.gov/publications/docs/standards-and-requirements/fpm/field_procedures_manual_2020.pdf)  
7. Adjustment Computations \- School of Earth Sciences \- The Ohio ..., accessed March 6, 2026, [https://earthsciences.osu.edu/sites/default/files/2021-02/OSU\_Adjustment\_Notes\_Part\_1.pdf](https://earthsciences.osu.edu/sites/default/files/2021-02/OSU_Adjustment_Notes_Part_1.pdf)  
8. STANDARDS OF COMPETENCE FOR CATEGORY "A" HYDROGRAPHIC SURVEYORS, accessed March 6, 2026, [https://iho.int/uploads/user/pubs/Drafts/S-5A\_Ed2.0.0.pdf](https://iho.int/uploads/user/pubs/Drafts/S-5A_Ed2.0.0.pdf)  
9. Analysis of GNSS, Hydroacoustic and Optoelectronic Data Integration Methods Used in Hydrography \- PMC, accessed March 6, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8659856/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659856/)  
10. Methodology for Combining Data Acquired by Unmanned Surface and Aerial Vehicles to Create Digital Bathymetric Models in Shallow and Ultra-Shallow Waters \- MDPI, accessed March 6, 2026, [https://www.mdpi.com/2072-4292/14/1/105](https://www.mdpi.com/2072-4292/14/1/105)  
11. 3D affine coordinate transformations, accessed March 6, 2026, [https://learning.aols.org/aols/3D\_Affine\_Coordinate\_Transformations.pdf](https://learning.aols.org/aols/3D_Affine_Coordinate_Transformations.pdf)  
12. Linear Algebra: Vector Spaces and Linear Transformations \- AMS Bookstore, accessed March 6, 2026, [https://bookstore.ams.org/amstext-57](https://bookstore.ams.org/amstext-57)  
13. What are differences between affine space and vector space? \- Math Stack Exchange, accessed March 6, 2026, [https://math.stackexchange.com/questions/884666/what-are-differences-between-affine-space-and-vector-space](https://math.stackexchange.com/questions/884666/what-are-differences-between-affine-space-and-vector-space)  
14. What are differences between affine space and vector space? | Wyzant Ask An Expert, accessed March 6, 2026, [https://www.wyzant.com/resources/answers/602352/what-are-differences-between-affine-space-and-vector-space](https://www.wyzant.com/resources/answers/602352/what-are-differences-between-affine-space-and-vector-space)  
15. Vector space vs Affine space concerning Force vectors in Intro Physics : r/mathematics \- Reddit, accessed March 6, 2026, [https://www.reddit.com/r/mathematics/comments/16xpu6u/vector\_space\_vs\_affine\_space\_concerning\_force/](https://www.reddit.com/r/mathematics/comments/16xpu6u/vector_space_vs_affine_space_concerning_force/)  
16. A. Vector and affine spaces \- LSE, accessed March 6, 2026, [https://personal.lse.ac.uk/robert49/PPB/pdf/DewarAppendicesBiblio.V52Oct20.pdf](https://personal.lse.ac.uk/robert49/PPB/pdf/DewarAppendicesBiblio.V52Oct20.pdf)  
17. Affine transformation \- Wikipedia, accessed March 6, 2026, [https://en.wikipedia.org/wiki/Affine\_transformation](https://en.wikipedia.org/wiki/Affine_transformation)  
18. 17\. Orthogonal Projections and Their Applications \- Quantitative Economics with Julia, accessed March 6, 2026, [https://julia.quantecon.org/tools\_and\_techniques/orth\_proj.html](https://julia.quantecon.org/tools_and_techniques/orth_proj.html)  
19. 3d coordinate transformations \- myGeodesy, accessed March 6, 2026, [http://www.mygeodesy.id.au/documents/Rotations2.pdf](http://www.mygeodesy.id.au/documents/Rotations2.pdf)  
20. Yaw, pitch, and roll rotations \- Steven M. LaValle, accessed March 6, 2026, [https://msl.cs.uiuc.edu/planning/node102.html](https://msl.cs.uiuc.edu/planning/node102.html)  
21. The Surveyor's Applications for Least Squares Adjustment (SALSA) User's Manual \- Applied Research Laboratories \- The University of Texas at Austin, accessed March 6, 2026, [https://wwwext.arlut.utexas.edu/salsa/pdfs/SalsaUserManual-6-2025.pdf](https://wwwext.arlut.utexas.edu/salsa/pdfs/SalsaUserManual-6-2025.pdf)  
22. Analyze the least-squares adjustment results—ArcGIS Pro | Documentation, accessed March 6, 2026, [https://pro.arcgis.com/en/pro-app/latest/help/data/parcel-editing/analyzeadjustmentresults.htm](https://pro.arcgis.com/en/pro-app/latest/help/data/parcel-editing/analyzeadjustmentresults.htm)  
23. Use of Total Least Squares Adjustment in Geodetic Applications \- MDPI, accessed March 6, 2026, [https://www.mdpi.com/2076-3417/14/6/2516](https://www.mdpi.com/2076-3417/14/6/2516)  
24. ADJUSTMENT COMPUTATIONS \- Purdue University, accessed March 6, 2026, [https://engineering.purdue.edu/\~bethel/adjcmp.pdf](https://engineering.purdue.edu/~bethel/adjcmp.pdf)  
25. Linear Transformations on Vector Spaces \- Open Textbook Library, accessed March 6, 2026, [https://open.umn.edu/opentextbooks/textbooks/linear-transformations-on-vector-spaces](https://open.umn.edu/opentextbooks/textbooks/linear-transformations-on-vector-spaces)  
26. Projection (linear algebra) \- Wikipedia, accessed March 6, 2026, [https://en.wikipedia.org/wiki/Projection\_(linear\_algebra)](https://en.wikipedia.org/wiki/Projection_\(linear_algebra\))  
27. STANDARDS OF COMPETENCE FOR CATEGORY "B" HYDROGRAPHIC SURVEYORS \- IHO, accessed March 6, 2026, [https://iho.int/iho\_pubs/standard/S-5/S-5B\_Ed1.0.1.pdf](https://iho.int/iho_pubs/standard/S-5/S-5B_Ed1.0.1.pdf)  
28. Linear Algebra 6.2.2 Orthogonal Projections \- YouTube, accessed March 6, 2026, [https://www.youtube.com/watch?v=fqbwErsP8Xw](https://www.youtube.com/watch?v=fqbwErsP8Xw)  
29. 3D rotation group \- Wikipedia, accessed March 6, 2026, [https://en.wikipedia.org/wiki/3D\_rotation\_group](https://en.wikipedia.org/wiki/3D_rotation_group)  
30. Linear Algebra 6.2.2 Orthogonal Projection \- YouTube, accessed March 6, 2026, [https://www.youtube.com/watch?v=np0d-HtJPqk](https://www.youtube.com/watch?v=np0d-HtJPqk)  
31. Algorithms for Ellipsoids \- Cornell University, accessed March 6, 2026, [https://tcg.mae.cornell.edu/pubs/Pope\_FDA\_08.pdf](https://tcg.mae.cornell.edu/pubs/Pope_FDA_08.pdf)  
32. \[2410.21217\] Symmetric similarity 3D coordinate transformation based on dual quaternion algorithm \- arXiv, accessed March 6, 2026, [https://arxiv.org/abs/2410.21217](https://arxiv.org/abs/2410.21217)  
33. Part III — Composing Rotations: Euler Angles and Roll–Pitch–Yaw \- Medium, accessed March 6, 2026, [https://medium.com/@sepideh.92sh/part-iii-composing-rotations-euler-angles-and-roll-pitch-yaw-38aa816a5bcd](https://medium.com/@sepideh.92sh/part-iii-composing-rotations-euler-angles-and-roll-pitch-yaw-38aa816a5bcd)  
34. Orientation / Rotations representation \- SBG Systems Support, accessed March 6, 2026, [https://support.sbg-systems.com/sc/kb/latest/underlying-maths-conventions/orientation-rotations-representation](https://support.sbg-systems.com/sc/kb/latest/underlying-maths-conventions/orientation-rotations-representation)  
35. matrices \- Yaw, Pitch and Roll composition \- Mathematics Stack Exchange, accessed March 6, 2026, [https://math.stackexchange.com/questions/3242495/yaw-pitch-and-roll-composition](https://math.stackexchange.com/questions/3242495/yaw-pitch-and-roll-composition)  
36. Orthogonal Projection, accessed March 6, 2026, [https://textbooks.math.gatech.edu/ila/projections.html](https://textbooks.math.gatech.edu/ila/projections.html)  
37. Orthogonal projection of points in CAD/CAM applications: an overview \- Oxford Academic, accessed March 6, 2026, [https://academic.oup.com/jcde/article/1/2/116/5743530](https://academic.oup.com/jcde/article/1/2/116/5743530)  
38. Given an implicit 3D plane, how do I find the orthogonal projection matrix \- which projects any point \- onto this plane? \- Math Stack Exchange, accessed March 6, 2026, [https://math.stackexchange.com/questions/646064/given-an-implicit-3d-plane-how-do-i-find-the-orthogonal-projection-matrix-whi](https://math.stackexchange.com/questions/646064/given-an-implicit-3d-plane-how-do-i-find-the-orthogonal-projection-matrix-whi)  
39. Orthogonal projection of an ellipsoid \[closed\] \- Math Stack Exchange, accessed March 6, 2026, [https://math.stackexchange.com/questions/3073718/orthogonal-projection-of-an-ellipsoid](https://math.stackexchange.com/questions/3073718/orthogonal-projection-of-an-ellipsoid)  
40. Orthogonal Projection onto an Ellipsoid \- Mathematics Stack Exchange, accessed March 6, 2026, [https://math.stackexchange.com/questions/1586207/orthogonal-projection-onto-an-ellipsoid](https://math.stackexchange.com/questions/1586207/orthogonal-projection-onto-an-ellipsoid)  
41. Vector-Algebra Algorithms to Draw the Curve of Alignment, the Great Ellipse, the Normal Section, and the Loxodrome \- MDPI, accessed March 6, 2026, [https://www.mdpi.com/2673-7418/4/2/8](https://www.mdpi.com/2673-7418/4/2/8)  
42. Helmert transformation \- Wikipedia, accessed March 6, 2026, [https://en.wikipedia.org/wiki/Helmert\_transformation](https://en.wikipedia.org/wiki/Helmert_transformation)  
43. Transformation parameters, plate motion models and deformation models \- UN-GGIM, accessed March 6, 2026, [https://ggim.un.org/UNGGCE/documents/CDWA/1/3\_1\_1%20-%20Development%20of%20transformation%20parameters.pdf](https://ggim.un.org/UNGGCE/documents/CDWA/1/3_1_1%20-%20Development%20of%20transformation%20parameters.pdf)  
44. Coordinate Transformations \- FIG, accessed March 6, 2026, [https://www.fig.net/resources/proceedings/fig\_proceedings/athens/papers/ts07/ts07\_2\_mitsakaki.pdf](https://www.fig.net/resources/proceedings/fig_proceedings/athens/papers/ts07/ts07_2_mitsakaki.pdf)  
45. Transformation parameters, plate motion models and deformation models \- UN-GGIM, accessed March 6, 2026, [https://ggim.un.org/UNGGCE/documents/CDWA-PAC/2\_3\_1%20-%20Development%20of%20transformation%20parameters.pdf](https://ggim.un.org/UNGGCE/documents/CDWA-PAC/2_3_1%20-%20Development%20of%20transformation%20parameters.pdf)  
46. Two-dimensional coordinate transformation, accessed March 6, 2026, [https://feng.stafpu.bu.edu.eg/Surveying%20Engineering/897/crs-18549/Files/Photo%20Lec%206%202020-2021-fin.pdf](https://feng.stafpu.bu.edu.eg/Surveying%20Engineering/897/crs-18549/Files/Photo%20Lec%206%202020-2021-fin.pdf)  
47. 2D Affine Transformation Parameters | PDF | Scientific Observation | Infographics \- Scribd, accessed March 6, 2026, [https://www.scribd.com/document/400876224/Affine-Transformation](https://www.scribd.com/document/400876224/Affine-Transformation)  
48. Example 5 \- 2D Helmert Similarity Transformation | PDF | Matrix (Mathematics) \- Scribd, accessed March 6, 2026, [https://www.scribd.com/document/334163852/Example-5-2D-Helmert-Similarity-Transformation](https://www.scribd.com/document/334163852/Example-5-2D-Helmert-Similarity-Transformation)  
49. COORDINATE TRANSFORMATIONS IN SURVEYING \- myGeodesy, accessed March 6, 2026, [http://www.mygeodesy.id.au/documents/COTRAN\_1.pdf](http://www.mygeodesy.id.au/documents/COTRAN_1.pdf)  
50. 2D affine transform parameters by Gaussian elimination with pivoting \- Archives of Civil Engineering, accessed March 6, 2026, [https://ace.il.pw.edu.pl/pdf-189148-126158?filename=2D%20affine%20transform.pdf](https://ace.il.pw.edu.pl/pdf-189148-126158?filename=2D+affine+transform.pdf)  
51. Transformation of 3D Co-ordinates, accessed March 6, 2026, [https://www.unsw.edu.au/content/dam/pdfs/engineering/civil-environmental/sage/teaching-and-learning/textbook-and-theses/Trans\_3D\_Aust\_Surv\_86.pdf](https://www.unsw.edu.au/content/dam/pdfs/engineering/civil-environmental/sage/teaching-and-learning/textbook-and-theses/Trans_3D_Aust_Surv_86.pdf)  
52. Practical Notes on Coordinate Transformation \- Swift Navigation, accessed March 6, 2026, [https://www.swiftnav.com/wp-content/uploads/2025/03/datum\_transformation\_march\_2020.pdf](https://www.swiftnav.com/wp-content/uploads/2025/03/datum_transformation_march_2020.pdf)  
53. PERFORMING 3D SIMILARITY TRANSFORMATION WITH LARGE ROTATION ANGLES USING CONSTRAINED MULTIVARIATE TOTAL LEAST SQUARES \- Redalyc.org, accessed March 6, 2026, [https://www.redalyc.org/journal/3939/393965447004/html/](https://www.redalyc.org/journal/3939/393965447004/html/)  
54. Inconsistency / doc issue in conventions Coordinate Frame vs Position Vector for \+towgs84 vs \+proj=helmert \#1091 \- GitHub, accessed March 6, 2026, [https://github.com/OSGeo/PROJ/issues/1091](https://github.com/OSGeo/PROJ/issues/1091)  
55. Coordinate Frame rotation (geog3D domain) \- EPSG:1038, accessed March 6, 2026, [https://epsg.io/1038-method](https://epsg.io/1038-method)  
56. Coordinate Frame rotation (geocentric domain) \- EPSG:1032, accessed March 6, 2026, [https://epsg.io/1032-method](https://epsg.io/1032-method)  
57. IOGP Publication 373-7-2 – Geomatics Guidance Note number 7, part 2, accessed March 6, 2026, [https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf](https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf)  
58. General Total Least Squares Theory for Geodetic Coordinate Transformations \- MDPI, accessed March 6, 2026, [https://www.mdpi.com/2076-3417/10/7/2598](https://www.mdpi.com/2076-3417/10/7/2598)
