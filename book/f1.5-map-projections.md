# F1.5 Map Projections

The science of hydrographic surveying fundamentally relies on the precise determination of position and depth within the marine environment. However, the transition of spatial data from the physical, three-dimensional, and mathematically irregular surface of the Earth to a two-dimensional mathematical plane represents one of the most foundational and mathematically rigorous challenges in the geodetic sciences.1 In hydrographic operations, where the accurate determination of depth and position is critical for the safety of marine navigation, dredging operations, offshore engineering, and the mapping of the seafloor, a profound understanding of the properties, parameters, and localized distortions of map projections is absolutely paramount.1

A map projection is mathematically defined as a systematic algorithmic or functional relationship that transforms geodetic coordinates—specifically latitude (![][image1]) and longitude (![][image2]) situated on a designated reference ellipsoid—into planar, rectangular Cartesian coordinates, typically expressed as Eastings (![][image3]) and Northings (![][image4]).1 Because the Earth is best modeled geodetically as an oblate spheroid or an ellipsoid of revolution (such as WGS84 or GRS80), it constitutes a non-developable surface.2 By the rigorous principles of differential geometry, a sphere or ellipsoid cannot be mapped onto a flat plane without inducing tearing, stretching, shearing, or a combination thereof.6 Consequently, every map projection inherently introduces some form of systemic distortion.8

In accordance with the International Hydrographic Organization (IHO) S-5A Standards of Competence for Category "A" Hydrographic Surveyors, Section F1.5, senior hydrographic professionals must possess an exhaustive, mathematically robust understanding of map projections.3 This entails the capacity to definitively classify projection properties, compute local distortions, apply rigorous geodetic-to-grid corrections—such as meridian convergence, scale factors, and arc-to-chord adjustments—and expertly contrast worldwide cartographic frameworks like the Universal Transverse Mercator (UTM), Gauss-Krüger (GK), and Universal Polar Stereographic (UPS) systems.3 This report exhaustively details the theoretical frameworks and practical applications of map projections within the discipline of hydrographic surveying.

## **1\. Classification of Map Projection Properties**

Map projections are systematically categorized based on the specific geometric properties they preserve during the mathematical transformation from the curved reference ellipsoid to the flat projection plane.7 Because it is mathematically impossible to preserve all spatial properties (area, angle, distance, and direction) simultaneously across an entire map, a projection must be selected based on the specific operational requirements of the hydrographic or cartographic application.7 The properties of projections dictate how the physical world is warped, and this warping is often mathematically visualized using Tissot’s Indicatrix, a geometric tool that illustrates local distortion by showing how a perfectly circular infinitesimal area on the ellipsoid is deformed on the map.12

### **1.1 Conformal (Orthomorphic) Projections**

A conformal projection—historically referred to as an "orthomorphic" or "right shape" projection—is defined mathematically as a projection that preserves angles locally.1 In differential terms, the point scale factor at any given infinitely small location is independent of the azimuth or direction of measurement.5 This means that the Tissot’s Indicatrix remains a perfect circle at any location on the map, although the absolute size of the circle will change depending on its geographic location, reflecting scale variation.12

For hydrographic surveying and marine navigation, conformality is an absolute, non-negotiable prerequisite.4 Navigators and surveyors rely heavily on the precise measurement of angles between position lines, the plotting of vessel headings, and the accurate representation of the coastline's true shape. If a nautical chart were not conformal, a ![][image5] physical turn executed by a vessel in the physical world would not measure ![][image5] on the chart, which would render the chart virtually useless and highly dangerous for safe navigation.7 Therefore, nearly all major navigational and hydrographic mapping frameworks, including the normal Mercator, Transverse Mercator, Lambert Conformal Conic, and Stereographic projections, are strictly conformal.1

### Interactive Distortion Demonstration (Tissot's Indicatrix)

To calculate the distortion caused by map projections, we can analyze the scale factors along the meridian and parallel. This is mathematically modeled using **Tissot's Indicatrix**.



```python

import math



def calculate_plate_carree_distortion(lat_deg):

    """Calculates Tissot indicatrix semi-axes (a, b) and angular distortion (omega)

    for the Plate Carree (Equidistant Cylindrical) projection."""

    lat_rad = math.radians(lat_deg)

    

    h = 1.0  # Scale along meridian

    k = 1.0 / math.cos(lat_rad)  # Scale along parallel

    

    a = max(h, k)

    b = min(h, k)

    

    omega_rad = 2 * math.asin((a - b) / (a + b))

    omega_deg = math.degrees(omega_rad)

    return a, b, omega_deg



# Example: Distortion at 60 degrees North

a, b, omega = calculate_plate_carree_distortion(60.0)

print(f"At 60N - Semi-major axis a: {a:.2f}, Semi-minor axis b: {b:.2f}")

print(f"Max Angular Distortion: {omega:.2f} degrees")

```


### **1.2 Equal-Area (Equivalent) Projections**

Equal-area projections, also known as equivalent projections, preserve the mathematical property of area throughout the entirety of the map.7 In an equal-area projection, a specific physical object, such as a coin, placed anywhere on the map will cover the exact same amount of true terrestrial geographic area, regardless of whether it is placed near the equator or at the extreme high latitudes of the poles.7 Mathematically, this is achieved by ensuring that the product of the principal scale factors along the meridian (![][image6]) and the parallel (![][image7]) at any point equals exactly one.13 For example, in a cylindrical equal-area projection, if the scale along the meridian (![][image6]) is expressed as ![][image8], the scale along the parallel (![][image7]) must be ![][image9] to maintain equivalence.13

While preserving area is highly desirable for statistical mapping, environmental resource management, global geographical information systems (GIS), and political mapping (where showing countries in their true relative sizes is important), it comes at a severe cartographic cost: the extreme distortion of shape and angles.7 The Tissot’s Indicatrix on an equal-area map becomes a highly elongated ellipse in regions of high distortion. Because angles are fundamentally skewed and shapes are crushed or elongated, equal-area projections are strictly avoided in standard hydrographic navigation and high-precision marine positioning.11

### **1.3 Equidistant Projections**

Equidistant projections are engineered to preserve true scale (distance) between certain specific points or along specific lines.7 It is a mathematical impossibility for any map projection to preserve distance correctly in all directions across the entire map. Instead, an equidistant projection might preserve distances strictly along all meridians (e.g., the Equidistant Cylindrical projection) or strictly radially outward from a single central focal point (e.g., the Azimuthal Equidistant projection).4

In hydrography and marine engineering, azimuthal equidistant projections are occasionally utilized for specialized applications. These include acoustic positioning reference displays, radio direction finding, seismic survey planning, or mapping exact distances from a central port, tsunami warning buoy, or subsea sonar array.1 In these highly specific use cases, knowing the exact distance from the center point is more critical than preserving local shape or overall area.

### **1.4 Azimuthal (Zenithal) Projections**

An azimuthal projection—sometimes called a zenithal projection—maintains true directions (azimuths) from a single central point to all other points on the map.13 In an azimuthal projection, the surface of the ellipsoid is mathematically projected directly onto a flat plane that is tangent to the Earth at a specific point.8 The defining characteristic of an azimuthal projection is that all great circles passing through the central point of tangency are represented as perfectly straight lines on the map.16

Azimuthal projections are not mutually exclusive from the other categories; they can be modified to be simultaneously conformal (such as the Stereographic projection), equal-area (such as the Lambert Azimuthal Equal-Area projection), or equidistant (such as the Azimuthal Equidistant projection).11

| Projection Property | Primary Preservation | Hydrographic Utility | Mathematical Characteristic | Common Examples |
| :---- | :---- | :---- | :---- | :---- |
| **Conformal** | Local angles and shapes | Essential for navigation and surveying | ![][image10] is independent of azimuth | Mercator, Transverse Mercator, Lambert Conformal Conic |
| **Equal-Area** | Relative areas | Environmental/Statistical mapping | ![][image11] | Albers Equal-Area, Lambert Azimuthal Equal-Area |
| **Equidistant** | Distance along specific lines | specialized ranging and acoustics | Scale is 1.0 along defined axes | Azimuthal Equidistant |
| **Azimuthal** | Direction from a central point | Polar charting, direction finding | Projected onto a tangent plane | Stereographic, Orthographic, Gnomonic |

## **2\. Properties and Applications of Developable Surfaces**

Beyond the geometric properties they preserve, map projections are primarily categorized by the mathematical surface onto which the ellipsoid is projected.8 These surfaces—specifically the cylinder, the cone, and the plane—are known as "developable surfaces" because, mathematically, they can be unrolled and laid completely flat without inducing any further distortion, stretching, or tearing.1 The manner in which these surfaces intersect or touch the reference ellipsoid dictates the resulting properties of the coordinate grid.

### **2.1 Cylindrical Projections**

Cylindrical projections conceptually wrap a mathematical cylinder around the reference ellipsoid. Once the points from the ellipsoid are projected onto the cylinder, the cylinder is sliced along its axis and unrolled into a flat rectangular plane. The orientation of the cylinder dictates the nature of the projection: if the cylinder is tangent to the equator, it is a normal cylindrical projection; if it is tangent to a meridian, it is a transverse cylindrical projection; and if it is tangent to any other arbitrary great circle, it is an oblique cylindrical projection.1

**The Normal Mercator Projection:** The standard Mercator projection, presented by Gerardus Mercator in 1569, is a normal, conformal cylindrical projection.12 The developable cylinder is tangent to the Earth at the Equator.4 The defining visual characteristic of the Mercator projection is its graticule: meridians and parallels are represented by two systems of perfectly straight lines intersecting at exactly right angles, forming a rectangular grid.4 To maintain conformality (the preservation of local shape), the spacing between parallels is mathematically increased as one approaches the poles, matching the natural convergence of the meridians on the globe.4

* *Hydrographic Application:* The most critical feature of the Mercator projection is that any straight line drawn on it represents a line of constant bearing or constant azimuth—known mathematically as a loxodrome or rhumb line.4 Because a ship's helmsman can set a constant compass heading and follow a straight line on the chart, the Mercator projection has been the absolute universal standard for marine nautical charts for centuries.4 However, the mathematical necessity of stretching the poles to infinity means that areal distortion becomes extreme at high latitudes, rendering the Mercator projection useless for polar navigation and heavily distorting the apparent size of high-latitude landmasses.16 It is considered highly accurate only within approximately ![][image12] of the Equator unless modified.16

**The Transverse Mercator (TM) Projection:** In the Transverse Mercator projection, also known as the Gauss-Krüger projection in its ellipsoidal form, the developable cylinder is mathematically rotated ![][image5] so that its axis lies within the equatorial plane.1 This makes the cylinder tangent to a specific selected line of longitude, which is designated as the central meridian.1 The result is a conformal projection where scale is constant (and often exact) along the central meridian, and distortion increases strictly as a function of the east-west distance from that meridian.1

* *Hydrographic Application:* Because distortion is practically negligible along the north-south axis, the TM projection is the ideal choice for mapping landmasses, coastal regions, and hydrographic survey zones that possess large north-south extents but narrow east-west spans.8 It forms the rigid mathematical backbone of global high-precision surveying systems like the Universal Transverse Mercator (UTM) and national frameworks like the New Zealand Transverse Mercator 2000 (NZTM2000) and various offshore island projections.4

**The Oblique Mercator Projection:** In the Oblique Mercator projection, the cylinder is tangent to an arbitrary great circle that is neither the equator nor a line of longitude.1 Linear scale remains true along this oblique line of tangency.16

* *Hydrographic Application:* This projection is uniquely utilized to map coastal features, island chains, or shipping channels that trend diagonally across the globe, such as the Aleutian Islands, the Hawaiian Islands, or the coastline of New Zealand, thereby minimizing scale distortion along that specific skewed navigational axis.1

### **2.2 Conical Projections**

Conical projections are generated by mathematically placing a cone over the reference ellipsoid.8 The apex of the cone is typically aligned with the Earth's axis of rotation. The cone can be tangent to a single parallel of latitude, or it can be secant, mathematically cutting through the ellipsoid at two specific standard parallels.1 When the cone is unrolled, the meridians appear as straight lines converging toward a single point (the apex of the cone), and the parallels are represented as concentric circular arcs with that apex as their common geometric center.13 The angle between the meridians is a mathematical fraction of the actual terrestrial longitude difference, a ratio known as the "constant of the cone" (![][image13]).13

**The Lambert Conformal Conic (LCC) Projection:** Introduced by Johann Heinrich Lambert in 1772, the LCC is a conformal projection that almost universally utilizes a secant cone, intersecting the ellipsoid at two standard parallels.1 The scale is exactly true (scale factor \= 1.0) along these two standard parallels.20 Between the two standard parallels, the scale factor drops slightly below 1.0 (meaning the map is slightly compressed relative to the Earth), and outside of the standard parallels, the scale factor increases above 1.0 (meaning the map is expanded).20

* *Hydrographic Application:* Because scale distortion in the LCC is solely a function of latitude and remains perfectly constant along any east-west line (parallel), the LCC is heavily utilized for regions with a massive east-west extent but a limited north-south extent.1 In the marine context, it is highly favored for coastal aeronautical charts, routing across the North Atlantic or Pacific (since a straight line on an LCC map very closely approximates a great circle route), and defining national spatial datasets, such as the United States State Plane Coordinate System (for states that are wide east-to-west like Tennessee) and the New Zealand Continental Shelf Lambert Conformal 2000 (NZCS2000) projection.8

**Polyconic Projections:** The American Polyconic projection, historically used extensively by the U.S. Coast and Geodetic Survey, is a complex class where parallels are represented by non-concentric circular arcs, with their centers falling on a straight central meridian.1 While scale is constant along the central meridian and along all parallels, the projection is not conformal, making it obsolete for modern precision hydrographic surveying, though it remains historically significant for cartography.1

### **2.3 Stereographic Projections**

The Stereographic projection belongs to the class of azimuthal (or zenithal) projections.1 Geometrically, it is formed by projecting points from the surface of the sphere or ellipsoid onto a tangent plane, with the perspective point of projection located at the antipodal point (the point on the sphere exactly diametrically opposite the point of tangency).4

The Stereographic projection possesses highly unique and valuable mathematical properties. It is the only projection in existence that is simultaneously azimuthal (preserving directions from the center) and conformal (preserving local angles and shapes).11 Another exceptional mathematical trait of the Stereographic projection is that it maps all circles on the surface of the sphere to true circles on the projection plane, regardless of their size or geographic location, whereas other projections would deform them into ellipses.11

* *Hydrographic Application:* The polar aspect of the Stereographic projection is an absolute necessity for polar hydrography and navigation.17 Because the standard Mercator projection cannot mathematically represent the poles (as the spacing of parallels stretches to infinity), and the Transverse Mercator suffers from extreme and unmanageable meridian convergence at very high latitudes, the Stereographic projection is uniquely suited for charting the Arctic and Antarctic regions.13 It serves as the foundational mathematics for the Universal Polar Stereographic (UPS) system.17

## **3\. Grids, Graticules, and Associated Coordinates**

To successfully position a hydrographic survey vessel, process acoustic bathymetric data, or delineate maritime legal boundaries, an absolute and rigorous framework for referencing spatial coordinates must be established.3 It is vital for Category "A" hydrographic surveyors to clearly differentiate between the concepts of graticules and grids, as they represent entirely different mathematical spaces.

### **3.1 The Graticule**

The graticule represents the geodetic coordinate system based on the angular measurements of latitude (![][image1]) and longitude (![][image2]) relative to a specific mathematical reference shape, typically an ellipsoid like WGS84 or GRS80.6

* **Latitude (![][image1]):** The angle between the equatorial plane and the straight line (normal) that passes through the point in question and intersects the polar axis.22  
* **Longitude (![][image2]):** The angle measured east or west from a reference prime meridian plane (typically Greenwich) to the meridian plane passing through the point.22

Graticules form a curved, intersecting network of non-parallel lines on the 3D surface. Meridians converge at the poles, and parallels differ continuously in circumference.6 While strictly accurate to the Earth's geometry, performing planar trigonometry, volumetric dredging computations, or localized distance measuring in angular sexagesimal units (degrees, minutes, seconds) is computationally heavy and practically non-intuitive for local engineering.6

### Interactive Projection Parameter Widget

We can visualize how projection parameters affect coordinates using Python's `ipywidgets`.



```{code-cell} ipython3

import ipywidgets as widgets

from IPython.display import display

from pyproj import Proj



def update_projection(lat_0=0.0, lon_0=0.0):

    # Create an Equidistant Cylindrical projection centered at lat_0, lon_0

    p = Proj(proj="eqc", lat_0=lat_0, lon_0=lon_0, ellps="WGS84")

    

    # Convert a test coordinate (e.g. 10 deg away from center)

    test_lon, test_lat = lon_0 + 10, lat_0 + 10

    x, y = p(test_lon, test_lat)

    

    print(f"Origin (lat_0={lat_0}, lon_0={lon_0})")

    print(f"Projected X for (+10deg lon, +10deg lat): {x:,.2f} m")

    print(f"Projected Y for (+10deg lon, +10deg lat): {y:,.2f} m")



# Create interactive sliders

widgets.interact(update_projection, 

                 lat_0=widgets.FloatSlider(min=-80, max=80, step=5, value=0),

                 lon_0=widgets.FloatSlider(min=-180, max=180, step=5, value=0));

```


### **3.2 The Grid**

A grid is a two-dimensional Cartesian coordinate system that is perfectly superimposed onto the flattened map projection surface.6 It consists of perfectly perpendicular lines representing linear units, uniformly expressed in meters (or occasionally international feet).8 Grid coordinates define a location using an ordered pair of linear values: Eastings (![][image3], measuring distance along the X-axis) and Northings (![][image4], measuring distance along the Y-axis).8

**False Origins:** To prevent the occurrence of negative coordinates—which can cause significant computational errors in geospatial databases, CAD software, and onboard real-time navigation systems—projections almost universally employ the concept of "false origins".8 By assigning an arbitrary, high numerical value to the true mathematical origin of the projection, all operational coordinates within the assigned zone remain positive integers.4

For example, the New Zealand Transverse Mercator 2000 (NZTM2000) projection utilizes a false origin of 10,000,000 meters North and 1,600,000 meters East.8 This not only ensures positive values but provides a distinctive numerical range that allows geospatial professionals to instantly identify the specific projection a set of coordinates belongs to.8

### Practical Implementation with Python (pyproj)

Hydrographers frequently perform coordinate transformations. In modern programming, the `pyproj` library (a python interface to PROJ) is the standard open-source tool for executing these operations robustly.



```python

from pyproj import Transformer



# Initialize a transformer from WGS84 (EPSG:4326) to UTM Zone 32N (EPSG:32632)

transformer = Transformer.from_crs("epsg:4326", "epsg:32632", always_xy=True)



# Convert longitude and latitude (e.g., Oslo, Norway)

lon, lat = 10.75, 59.91

easting, northing = transformer.transform(lon, lat)



print(f"UTM Zone 32N Easting: {easting:.2f} m, Northing: {northing:.2f} m")



# Convert back to WGS84

back_transformer = Transformer.from_crs("epsg:32632", "epsg:4326", always_xy=True)

orig_lon, orig_lat = back_transformer.transform(easting, northing)

print(f"Recovered WGS84 Longitude: {orig_lon:.4f}°, Latitude: {orig_lat:.4f}°")

```


### **3.3 Coordinate Conversions vs. Transformations**

The transition from the curved graticule to the planar grid is the explicit purpose of mapping equations.5 It is critical to distinguish between a *conversion* and a *transformation*:

* **Coordinate Conversion:** A mathematical change in format from geodetic coordinates (![][image14]) to grid coordinates (![][image15]) *within the exact same datum* (e.g., from WGS84 lat/lon to WGS84 UTM Zone 30N). This involves rigorous mapping equations but no shift in the underlying Earth model.  
* **Coordinate Transformation:** A shift from one geodetic datum to an entirely different geodetic datum (e.g., from historical NAD27 to modern WGS84). This requires datum shift parameters (such as a 3-parameter or 7-parameter Helmert transformation) because the origin, orientation, and scale of the underlying reference ellipsoids are fundamentally different.

## **4\. Geodetic to Grid Corrections (Computational Geodesy)**

When raw observational data is captured by a hydrographic survey vessel—be it true heading from a Fiber Optic Gyrocompass (FOG), raw distances from a laser scanner, or azimuths from an Inertial Navigation System (INS)—these physical measurements reflect the true reality of the geodetic ellipsoid.1 However, final survey deliverables, Electronic Navigational Charts (ENCs), and Geographic Information Systems (GIS) overwhelmingly utilize planar grids.1

Projecting physical observations directly onto a grid without accounting for the mathematical distortion of the projection introduces massive, systematic errors. Transforming these observations correctly requires the application of three fundamental corrections: Meridian Convergence (![][image16]), the Scale Factor (![][image10]), and the Arc-to-Chord Correction (![][image17]).5

### **4.1 Meridian Convergence (![][image16])**

Meridian convergence, frequently referred to as the mapping angle or grid declination, is the highly specific angular difference between true geodetic north (the direction to the geographic North Pole along the local meridian curve) and grid north (the direction perfectly parallel to the Y-axis of the Cartesian projection grid).5

Because all meridians physically converge at the poles on a sphere, but all grid north lines are mathematically forced to remain perfectly parallel to each other on a plane, grid north and true north only align perfectly at the central meridian of the projection.27 As a vessel travels east or west away from the central meridian, the angle of convergence systematically increases.27

**Mathematical Formulation:** A practical approximation for meridian convergence on a transverse cylindrical or conical projection is defined as: ![][image18] 10 Where ![][image19] is the difference in longitude from the central meridian, and ![][image1] is the latitude of the observation.10

However, for precise geodetic mapping and Category "A" hydrographic computations in the Transverse Mercator projection, a rigorous Taylor series expansion must be applied to account for the true ellipsoidal geometry. The rigorous formula derived from geographic coordinates is: ![][image20] 10 Where ![][image21] (with ![][image22] being the second eccentricity of the reference ellipsoid).5

Alternatively, if computed from existing grid coordinates, the convergence can be approximated as: ![][image23] 10 Where ![][image24] is the grid distance (Easting) from the central meridian, and ![][image25] is the radius of the Earth.10

**Sign Conventions:** Two distinct sign conventions govern the application of convergence 27:

1. **The Survey Convention** (standard in the Southern Hemisphere, including Australia and New Zealand): Grid convergence is defined as positive when grid north lies to the west of true north (which occurs when the point is east of the central meridian).27  
2. **The Gauss-Bomford Convention** (standard in North America and Europe): Defines convergence as the geodetic azimuth minus the projected grid azimuth on the coordinate grid. This often yields opposite algebraic signs to the Survey Convention depending on localized software implementations.5

**Hydrographic Significance:** Hydrographers must actively apply convergence to physical sensors.3 For instance, a vessel's INS or gyrocompass naturally seeks true geodetic north based on Earth's rotation and gravity.28 If this true heading data is ingested into an acquisition software operating on a UTM grid, the meridian convergence must be actively applied to compute the correct vessel grid heading. Failure to apply convergence will induce a systematic rotational yaw error across the entire swath of a Multibeam Echo Sounder (MBES), severely degrading cross-track positioning accuracy, particularly in deep water.3

### **4.2 Scale Factors (![][image10])**

Because the mathematical flattening of the Earth inherently requires stretching or compression of the surface, a physical distance measured on the ellipsoid (![][image26]) will almost never equal the calculated grid distance on the chart (![][image27]).1 The point scale factor (![][image10]) is defined mathematically as the ratio of the infinitely small grid distance to the true ellipsoidal distance: ![][image28] 10

For conformal map projections, the scale factor at any specific point is identical in all directions, which is the mechanism that ensures angles are maintained.5 However, ![][image10] is not a constant value across the map; it changes systematically as a function of the coordinates.5

**Calculating Scale in Transverse Mercator (UTM/GK):** In a transverse cylindrical projection, the scale factor is designated a specific fixed value at the central meridian (![][image29]).10 As one moves orthogonally away from the central meridian (along the Easting axis, ![][image24]), the scale factor increases quadratically. The formula utilizing grid coordinates is: ![][image30] 10 Where ![][image24] is the lateral grid distance from the central meridian, and ![][image25] is the geometric mean radius of curvature of the reference ellipsoid at that latitude.1

**Line Scale Factor (![][image31]):** While a point scale factor is valid for an infinitesimal location, hydrographic surveys deal with discrete baselines and ranges. Over long survey lines, the scale factor changes continuously from the start point to the end point. To obtain a highly accurate overall grid distance for the line, the Line Scale Factor (![][image31]) must be computed. This is often achieved using Simpson’s Rule for numerical integration: ![][image32] 25 Where ![][image33] is the scale factor at the origin of the line, ![][image34] is the scale factor at the terminus, and ![][image6] is the scale factor at the exact midpoint of the line.25

**Linear Distortion Evaluation:** For engineering-scale dredging surveys, breakwater construction, or precise subsea installations, the absolute linear distortion between the grid representations and actual physical dimensions must be rigorously quantified. It is expressed in parts per million (ppm) and must factor in both the projection scale factor (![][image10]) and the ellipsoidal height (![][image35]) of the project datum relative to the mean radius of curvature (![][image36]): ![][image37] 5 A hydrographer relies on these computations to transition from a measured acoustic range in the water column to an ellipsoidal reference, and subsequently project it onto the cartographic grid for payment volumes.

### **4.3 Arc-to-Chord Correction (![][image17] or ![][image38])**

The arc-to-chord correction, commonly denoted mathematically as ![][image38] or the "![][image17] correction," accounts for the curvature of the projected shortest path on the flat grid surface.5

When two points are connected by the absolute shortest possible physical distance on the curved ellipsoid, the resulting path is known as a geodetic curve or a geodesic.10 When this geodetic curve is projected onto a flat plane using a conformal mapping equation, it does not plot as a perfectly straight line.4 Instead, due to the projection's distortion, it plots as a subtle arc bowing toward the central meridian (in TM) or the standard parallel (in LCC).14 The straight line drawn between the two plotted points on the grid is the "chord."

The minute angle between the projected geodetic azimuth (![][image39]) and the straight grid azimuth (![][image40]) is the ![][image17] correction.10 The overarching mathematical relationship linking the physical geodetic azimuth (![][image41]), meridian convergence (![][image16]), and the arc-to-chord correction is defined as: ![][image42] 31 Where ![][image43].10

**Calculation of t-T:** For a Transverse Mercator projection, calculating the exact correction involves the Cartesian coordinates of the starting point (![][image44]) and the ending point (![][image45]). The primary rigorous formula is expressed as: ![][image46] 10 Where ![][image47] is the mean radius of curvature of the ellipsoid. A highly practical operational approximation used in rapid terrestrial survey computations determines the magnitude of the correction directly in seconds of arc: ![][image48] 31 Where ![][image49] is the distance from the central axis of the projection to the line's midpoint, and ![][image50] is the difference in eastings between the two endpoints, with both measured in meters.31

**Hydrographic Significance:** Historically, in conventional optical triangulation along coastlines, failure to apply the ![][image17] correction over sightlines of several kilometers resulted in massive angular misclosures.25 In modern hydrography, which is dominated by Global Navigation Satellite Systems (GNSS) executing computations inherently in 3D ECEF (Earth-Centered, Earth-Fixed) frameworks, the arc-to-chord correction is often seamlessly managed under the hood of acquisition software.36 However, an IHO Category "A" surveyor must explicitly understand and command these corrections during rigorous INS alignment routines, manual geodetic total station tie-ins to tide gauges, or when executing ultra-short baseline (USBL) acoustic subsea metrology traversing for offshore oil and gas infrastructure.3 Ignorance of the ![][image38] parameter systematically skews angular networks as the vectors lengthen.31

## **5\. Worldwide Cartographic Systems**

To standardize global mapping, facilitate international military and scientific cooperation, and avoid the sheer chaos of thousands of overlapping and incompatible local projections, international mapping bodies developed globally applicable, standardized cartographic grid systems.3 The three most dominant implementations in global hydrography are the Universal Transverse Mercator (UTM), Gauss-Krüger (GK), and Universal Polar Stereographic (UPS) grids.22

### **5.1 Universal Transverse Mercator (UTM)**

Developed heavily by the United States military corps in the mid-20th century, the UTM system provides a conformal, low-distortion coordinate framework for the vast majority of the navigable globe.40 It utilizes a family of secant Transverse Mercator projections.4

**System Specifications:**

* **Global Coverage:** The UTM grid strictly spans the latitudes from ![][image51] North to ![][image52] South.22 The asymmetry in latitude limits is designed specifically to accommodate the boundaries of important landmasses near the Arctic Ocean.14 Areas beyond these latitudes default to the UPS system.22  
* **Zone Architecture:** The globe is mathematically sliced into 60 discrete longitudinal zones, each exactly ![][image53] wide in longitude.22 Zone 1 originates at the antimeridian (![][image54] W) and extends to ![][image55] W, with numbering increasing sequentially eastward.22  
* **Central Meridian and Scale Factor:** Every ![][image53] zone possesses its own central meridian.22 To aggressively minimize scale distortion across the entire 6-degree width of the zone, UTM utilizes a secant cylinder geometry. This introduces a central scale factor (![][image29]) of **0.9996** exactly at the central meridian.4 Consequently, the line of true scale (![][image56]) lies approximately 180 km on either side of the central meridian, and maximum scale distortion at the extreme edges of the zone at the equator is strictly restrained to approximately 1 part in 1,000 (0.1%).40  
* **False Origin Coordinates:**  
  * **Eastings:** To avoid negative X-coordinates, the central meridian of every single zone is assigned a False Easting of 500,000 meters. Thus, a coordinate of 400,000m E immediately indicates a location exactly 100km west of the central axis.4  
  * **Northings (Northern Hemisphere):** The Equator is assigned a False Northing of 0 meters.22  
  * **Northings (Southern Hemisphere):** To mathematically prevent negative Y-values south of the equator, the Equator is assigned a massive False Northing of 10,000,000 meters.4

UTM represents the undisputed operational standard for coastal and offshore hydrographic surveys, offshore wind farm site investigations, and electronic navigation systems operating within the mid-latitudes.3

### **5.2 Gauss-Krüger (GK) System**

The Gauss-Krüger projection system is deeply rooted in European, Russian, and Asian cartography. It is mathematically parallel to the UTM system—as both operate on the exact same Transverse Mercator ellipsoidal geometry—but it differs in its structural execution and parameterization.18

**System Specifications:**

* **Zone Architecture:** GK systems operate on longitudinal zones that are predominantly ![][image57] or ![][image53] wide, allowing tighter operational control over distortion compared to UTM.18  
* **Scale Factor:** The most distinct mathematical differentiator is that Gauss-Krüger utilizes a tangent cylinder rather than a secant one. Thus, the central scale factor (![][image29]) is exactly **1.0000** at the central meridian.10 Because it lacks the secant reduction of UTM, distance distortion grows much more rapidly toward the zone edges. This rapid degradation is precisely why a narrower ![][image57] zone width is frequently favored in GK applications to mathematically restrict scale errors.18  
* **False Origins:** Like UTM, GK applies a False Easting of 500,000 meters to the central meridian.18 Uniquely, however, many national GK deployments append the zone number directly to the False Easting prefix. For instance, in Zone 5, the central meridian might be designated as 5,500,000 meters East, providing an instant identifier of the zone within the coordinate string itself.18

For a hydrographer operating in Eurasian waters, transitioning seamlessly between UTM and GK—and properly managing the severe scale factor shifts during datum transformations—is an essential competency.3

### **5.3 Universal Polar Stereographic (UPS)**

In the polar regions, the UTM grid mathematically destabilizes due to severe meridian convergence and the infinite stretching of the Transverse Mercator mathematics near the poles.14 To map these extreme latitudes, the Universal Polar Stereographic grid assumes command.14 Operating on a polar-aspect, conformal stereographic projection, the UPS specifically governs latitudes north of ![][image51] N and south of ![][image52] S.17

**System Specifications:**

* **Scale Factor:** The projection plane operates as a secant plane, mathematically intersecting the reference ellipsoid at a latitude of true scale at approximately ![][image58] North or South.17 To distribute scale distortion optimally across the polar cap, the point scale factor at the precise geometric pole is mandated as **0.994**.17  
* **Grid Orientation and Origins:**  
  * The geographic North and South poles act as the functional centers of their respective grids. Each pole is assigned a False Easting of 2,000,000 meters and a False Northing of 2,000,000 meters to ensure positive coordinate geometry.17  
  * The Y-axis aligns rigidly with the ![][image59] prime meridian line.22 In the North zone, moving along the ![][image54] meridian away from the pole increases the Northing value.22  
  * The X-axis aligns precisely with the ![][image5] E / ![][image5] W meridians.22  
* **Overlap:** To prevent dangerous navigational boundary issues and software faults for vessels operating on the margins of the systems, the UPS system deliberately overlaps the UTM framework by 30 minutes of latitude (extending down to ![][image60] N and up to ![][image61] S).39

| Feature | Universal Transverse Mercator (UTM) | Gauss-Krüger (GK) | Universal Polar Stereographic (UPS) |
| :---- | :---- | :---- | :---- |
| **Projection Mathematics** | Transverse Cylindrical (Secant) | Transverse Cylindrical (Tangent) | Azimuthal Stereographic (Secant) |
| **Global Extent** | 80° S to 84° N | Global (Predominantly Eurasian) | Poles to 80° S / 84° N |
| **Zone Width** | 6° Longitude | 3° or 6° Longitude | Polar Caps (2 Zones total) |
| **Central Scale Factor (![][image29])** | 0.9996 | 1.0000 | 0.9940 at geometric Pole |
| **False Easting** | 500,000 m | 500,000 m (+ Zone Prefix option) | 2,000,000 m |
| **False Northing** | 0 m (North), 10,000,000 m (South) | 0 m | 2,000,000 m |

## **6\. Practical Execution and Geometrical Analysis in Hydrographic Operations**

Understanding the geometric behavior and mathematical nuances of map projections translates directly to the real-world management of spatial uncertainties, the meticulous planning of acoustic data acquisition, and the execution of legal hydrographic responsibilities required of a Category "A" surveyor.1

### **6.1 Positioning and High-Precision Sensor Integration**

A modern hydrographic survey suite is an incredibly complex assembly of highly discrete sensors operating in differing spatial reference frames.3 An Inertial Navigation System (INS) outputs orientation (roll, pitch, and heading) based on gravity and true geodetic north. GNSS receivers yield positions in 3D ellipsoidal coordinates (![][image1], ![][image2], ![][image35]).3 Meanwhile, the hydrographic acquisition software logs, filters, and visualizes the sonar swaths on a projected Cartesian plane (such as UTM).1

If the acquisition software projects the GNSS coordinates to a UTM grid, but fails to apply the necessary meridian convergence (![][image16]) algorithm to the INS gyro heading, the entire multibeam swath will be rotated relative to the grid. This introduces severe cross-track positioning errors that amplify linearly as water depth (and thus swath width) increases.10 A Category "A" surveyor must configure, validate, and mathematically audit the rigorous application of these geodetic-to-grid rotation matrices to ensure S-44 survey standards are met.3

### **6.2 Managing Cartographic Boundary Discontinuities**

When a continuous hydrographic survey transcends a UTM or GK zone boundary, severe geometric discontinuities arise.22 Because each discrete zone utilizes a completely unique central meridian, adjacent zones possess entirely different mathematical projection planes. Survey lines that are perfectly straight in UTM Zone 30 will fracture, kink, or display angular offsets when extended natively into UTM Zone 31\.39

To manage this complex topological issue, hydrographers employ several strategies. They may extend the parameters of one zone beyond its ![][image53] limit for the duration of the localized project, accepting the elevated scale distortion in exchange for a unified coordinate system. Alternatively, they transition the dataset entirely to an oblique projection or a secant conic projection (like the LCC) to envelop the entire survey area under a single, unified coordinate space that natively mitigates the boundary fault.1

### **6.3 Volumetric Analysis and Metrological Accuracy**

In precision dredging operations, port construction, or subsea engineering, volumetric analysis and metrology strictly govern financial payment and structural integrity.3 Because map projection scale factors fundamentally alter grid distances relative to true physical terrestrial lengths, a distance measured acoustically underwater by a sonar must be corrected via the line scale factor (![][image31]) prior to executing grid coordinate geometry operations.25

Using a grid distance directly from uncorrected UTM coordinates to pre-cut physical subsea pipelines or to measure precise dredge volumes over extensive areas will yield measurable deficits and severe financial liability. Rigorously calculating linear distortion and applying arc-to-chord (![][image17]) corrections guarantees that theoretical engineering models align perfectly with the physical oceanographic realities of the deployment.5

In conclusion, the mapping of the hydrographic environment depends entirely upon the robust mathematical translation of a curved Earth onto a navigable, mathematically sound planar surface. Through a deep, academic mastery of the IHO S-5A Section F1.5 syllabus—encompassing the differential geometry of conformal, equal-area, and stereographic planes, as well as the calculation of convergence, scale factors, and arc-to-chord constraints—the hydrographic surveyor guarantees the spatial integrity of all marine data.3 Whether maneuvering through the highly specific scale architectures of the UTM and Gauss-Krüger transverse cylinders, or conducting operations in the extreme high-latitude domains of the UPS system, the hydrographer expertly mitigates the inevitable distortions of mapping equations to produce charts and models that assure the absolute safety of global navigation.1

#### **Works cited**

1. Coordinate Conversion for Hydrographic Surveying, accessed March 1, 2026, [https://www.ngs.noaa.gov/PUBS\_LIB/CoordinateCoversionforHydrographicSurveying\_TR\_NOS114\_CGS7.pdf](https://www.ngs.noaa.gov/PUBS_LIB/CoordinateCoversionforHydrographicSurveying_TR_NOS114_CGS7.pdf)  
2. Map Projection Design \- State Cartographer's Office, accessed March 1, 2026, [https://www.sco.wisc.edu/wp-content/uploads/2020/02/Map-Projection-Design-WSRS2022.pdf](https://www.sco.wisc.edu/wp-content/uploads/2020/02/Map-Projection-Design-WSRS2022.pdf)  
3. S-5A\_Ed1.0.2.pdf  
4. INTERNATIONAL HYDROGRAPHIC ORGANIZATION \- C-13\_e1.0.0 ..., accessed March 1, 2026, [https://www.deparentis.com/wp-content/uploads/2020/04/IHO-Manual-on-Hydrography-1st-edition-February-2011-C-13\_e1.0.0\_ENG.pdf](https://www.deparentis.com/wp-content/uploads/2020/04/IHO-Manual-on-Hydrography-1st-edition-February-2011-C-13_e1.0.0_ENG.pdf)  
5. map projection functions, accessed March 1, 2026, [https://www.sco.wisc.edu/wp-content/uploads/2020/02/Map-Projection-Functions-WSRS2022.pdf](https://www.sco.wisc.edu/wp-content/uploads/2020/02/Map-Projection-Functions-WSRS2022.pdf)  
6. 2.3 What are Map Projections? | GEOG 160 \- Dutton Institute, accessed March 1, 2026, [https://www.e-education.psu.edu/geog160/node/1918](https://www.e-education.psu.edu/geog160/node/1918)  
7. Choose the right projection | Documentation \- Learn ArcGIS, accessed March 1, 2026, [https://learn.arcgis.com/en/projects/choose-the-right-projection/](https://learn.arcgis.com/en/projects/choose-the-right-projection/)  
8. Projections | Geodetic Guidance \- LINZ, accessed March 1, 2026, [https://www.linz.govt.nz/guidance/geodetic-system/coordinate-systems-used-new-zealand/projections](https://www.linz.govt.nz/guidance/geodetic-system/coordinate-systems-used-new-zealand/projections)  
9. Standards of Competence for Category "A" Hydrographic Surveyors (Preview PR) \- GitHub Pages, accessed March 1, 2026, [https://metanorma.github.io/mn-samples-iho/documents/s5a/document.pdf](https://metanorma.github.io/mn-samples-iho/documents/s5a/document.pdf)  
10. CHAPTER 2 POSITIONING \- IHO, accessed March 1, 2026, [https://iho.int/uploads/user/pubs/cb/c-13/english/C-13\_Chapter\_2.pdf](https://iho.int/uploads/user/pubs/cb/c-13/english/C-13_Chapter_2.pdf)  
11. Stereographic projection \- Wikipedia, accessed March 1, 2026, [https://en.wikipedia.org/wiki/Stereographic\_projection](https://en.wikipedia.org/wiki/Stereographic_projection)  
12. Transverse Mercator projection \- Wikipedia, accessed March 1, 2026, [https://en.wikipedia.org/wiki/Transverse\_Mercator\_projection](https://en.wikipedia.org/wiki/Transverse_Mercator_projection)  
13. A Study of Map Projections in General \- National Geodetic Survey ..., accessed March 1, 2026, [https://geodesy.noaa.gov/library/pdfs/Special\_Publication\_No\_60.pdf](https://geodesy.noaa.gov/library/pdfs/Special_Publication_No_60.pdf)  
14. UTM and UPS \- Naval Postgraduate School, accessed March 1, 2026, [https://www.oc.nps.edu/oc2902w/maps/utmups.pdf](https://www.oc.nps.edu/oc2902w/maps/utmups.pdf)  
15. Lambert conformal conic—ArcGIS Pro | Documentation, accessed March 1, 2026, [https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/lambert-conformal-conic.htm](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/lambert-conformal-conic.htm)  
16. THE PROPERTIES AND USES OF SELECTED MAP PROJECTIONS \- USGS Publications Warehouse, accessed March 1, 2026, [https://pubs.usgs.gov/pp/1395/plate-1.pdf](https://pubs.usgs.gov/pp/1395/plate-1.pdf)  
17. Stereographic—ArcGIS Pro | Documentation, accessed March 1, 2026, [https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/stereographic.htm](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/stereographic.htm)  
18. Gauss-Krüger—ArcGIS Pro | Documentation, accessed March 1, 2026, [https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/gauss-kruger.htm](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/gauss-kruger.htm)  
19. Transverse Mercator—ArcGIS Pro | Documentation, accessed March 1, 2026, [https://pro.arcgis.com/en/pro-app/3.4/help/mapping/properties/transverse-mercator.htm](https://pro.arcgis.com/en/pro-app/3.4/help/mapping/properties/transverse-mercator.htm)  
20. Lambert conformal conic projection \- Wikipedia, accessed March 1, 2026, [https://en.wikipedia.org/wiki/Lambert\_conformal\_conic\_projection](https://en.wikipedia.org/wiki/Lambert_conformal_conic_projection)  
21. Chart Projections \- Jeppesen, accessed March 1, 2026, [https://jsumsweb.jeppesen.com/FliteStar/Help/Chart\_Projections.htm](https://jsumsweb.jeppesen.com/FliteStar/Help/Chart_Projections.htm)  
22. NGA Geomatics \- Coordinate Systems, accessed March 1, 2026, [https://earth-info.nga.mil/index.php?dir=coordsys\&action=coordsys](https://earth-info.nga.mil/index.php?dir=coordsys&action=coordsys)  
23. Grids and graticules—ArcGIS Pro | Documentation, accessed March 1, 2026, [https://pro.arcgis.com/en/pro-app/latest/help/layouts/grids-and-graticules.htm](https://pro.arcgis.com/en/pro-app/latest/help/layouts/grids-and-graticules.htm)  
24. Transverse Mercator—ArcMap | Documentation, accessed March 1, 2026, [https://desktop.arcgis.com/en/arcmap/latest/map/projections/transverse-mercator.htm](https://desktop.arcgis.com/en/arcmap/latest/map/projections/transverse-mercator.htm)  
25. A MANUAL FOR GEODETIC POSITION COMPUTATIONS IN THE MARITIME PROVINCES \- Geodesy & Geomatics Engineering, accessed March 1, 2026, [https://gge.ext.unb.ca/Pubs/TR52.pdf](https://gge.ext.unb.ca/Pubs/TR52.pdf)  
26. MAP PROJECTIONS FOR ELECTRONIC NAVIGATION AND OTHER MARINE GIS APPLICATIONS \- Centre for Digital Scholarship Journals, accessed March 1, 2026, [https://journals.lib.unb.ca/index.php/ihr/article/download/20958/24133/29779](https://journals.lib.unb.ca/index.php/ihr/article/download/20958/24133/29779)  
27. Convergence, scale factors and declination | Geodetic Guidance \- LINZ, accessed March 1, 2026, [https://www.linz.govt.nz/guidance/geodetic-system/coordinate-systems-used-new-zealand/projections/convergence-scale-factors-and-declination](https://www.linz.govt.nz/guidance/geodetic-system/coordinate-systems-used-new-zealand/projections/convergence-scale-factors-and-declination)  
28. Grid and Geodetic Azimuths | GEOG 862: GPS and GNSS for Geospatial Professionals, accessed March 1, 2026, [https://www.e-education.psu.edu/geog862/node/1816](https://www.e-education.psu.edu/geog862/node/1816)  
29. Meridian Convergence | PDF \- Scribd, accessed March 1, 2026, [https://www.scribd.com/document/716505731/MERIDIAN-CONVERGENCE](https://www.scribd.com/document/716505731/MERIDIAN-CONVERGENCE)  
30. The Patch Test \- Multibeam Calibration \- R2Sonic, accessed March 1, 2026, [https://www.r2sonic.com/wp-content/uploads/2020/03/The-New-Patch-Test.pdf](https://www.r2sonic.com/wp-content/uploads/2020/03/The-New-Patch-Test.pdf)  
31. State Plane Coordinate System of 1983 \- National Geodetic Survey (NGS), accessed March 1, 2026, [https://geodesy.noaa.gov/library/pdfs/NOAA\_Manual\_NOS\_NGS\_0005.pdf](https://geodesy.noaa.gov/library/pdfs/NOAA_Manual_NOS_NGS_0005.pdf)  
32. Please Help: T-t Correction or Arc-To-Chord Correction \- Google Groups, accessed March 1, 2026, [https://groups.google.com/g/sci.engr.surveying/c/r2A3YOMjz7E](https://groups.google.com/g/sci.engr.surveying/c/r2A3YOMjz7E)  
33. 4\. Meridian Convergence \- Page 4 \- Open Access Surveying Library, accessed March 1, 2026, [https://jerrymahun.com/index.php/home/open-access/32-vi-directions/265-chapter-c-meridian-conversion?start=3](https://jerrymahun.com/index.php/home/open-access/32-vi-directions/265-chapter-c-meridian-conversion?start=3)  
34. PART IV: COORDINATES AND MAP PROJECTIONS \- MDOT Public Applications, accessed March 1, 2026, [https://mdotjboss.state.mi.us/stdplan/getStandardPlanDocument.htm?docGuid=3bc20f59-1df5-4145-9456-21105890082f](https://mdotjboss.state.mi.us/stdplan/getStandardPlanDocument.htm?docGuid=3bc20f59-1df5-4145-9456-21105890082f)  
35. 2.2.2 Control survey with traveses or triangulation \- 1\) General \- JICA Report PDF, accessed March 1, 2026, [https://openjicareport.jica.go.jp/pdf/10731255\_02.pdf](https://openjicareport.jica.go.jp/pdf/10731255_02.pdf)  
36. SPC arc to chord correction \- Discussion Forums \- RPLS.com, accessed March 1, 2026, [https://rpls.com/forums/strictly-surveying/spc-arc-to-chord-correction/](https://rpls.com/forums/strictly-surveying/spc-arc-to-chord-correction/)  
37. Standards and Procedures for Referencing Project Elevation Grades to Nationwide Vertical Datums \- USACE Publications \- U.S. Army, accessed March 1, 2026, [https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em\_1110-2-6056.pdf](https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em_1110-2-6056.pdf)  
38. (PDF) GPS Alignment Surveys and Meridian Convergence \- ResearchGate, accessed March 1, 2026, [https://www.researchgate.net/publication/265626011\_GPS\_Alignment\_Surveys\_and\_Meridian\_Convergence](https://www.researchgate.net/publication/265626011_GPS_Alignment_Surveys_and_Meridian_Convergence)  
39. Universal Transverse Mercator (UTM) and Universal Polar Stereographic (UPS). Edition 1 \- DTIC, accessed March 1, 2026, [https://apps.dtic.mil/sti/tr/pdf/ADA266497.pdf](https://apps.dtic.mil/sti/tr/pdf/ADA266497.pdf)  
40. Universal Transverse Mercator coordinate system \- Wikipedia, accessed March 1, 2026, [https://en.wikipedia.org/wiki/Universal\_Transverse\_Mercator\_coordinate\_system](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)  
41. Understanding the Difference between Map Projection vs. Coordinate System \- Inertial Labs, accessed March 1, 2026, [https://inertiallabs.com/understanding-the-difference-between-map-projections-vs-coordinate-systems/](https://inertiallabs.com/understanding-the-difference-between-map-projections-vs-coordinate-systems/)  
42. Basics of the Gauss-Krüger Coordinate System | Sven Ruppert, accessed March 1, 2026, [https://svenruppert.com/2024/05/16/basics-of-the-gauss-kruger-coordinate-system/](https://svenruppert.com/2024/05/16/basics-of-the-gauss-kruger-coordinate-system/)  
43. Hydrographic Surveying \- USACE Publications, accessed March 1, 2026, [https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM\_1110-2-1003.pdf](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1003.pdf)  
44. assessment of the accuracies of multibeam calibration values and the depth between real-time kinematics and precise point positioning \- Unilorin JOGER, accessed March 1, 2026, [https://unilorinjoger.com/wp-content/uploads/2025/04/BASIL-D.D.-ASSESSMENT-OF-THE-ACCURACIES-OF-MULTIBEAM-CALIBRATION-VALUES-AND-THE-DEPTH-BETWEEN-REAL-TIME-KINEMATICS-AND-PRECISE-POINT-POSITIONING.pdf](https://unilorinjoger.com/wp-content/uploads/2025/04/BASIL-D.D.-ASSESSMENT-OF-THE-ACCURACIES-OF-MULTIBEAM-CALIBRATION-VALUES-AND-THE-DEPTH-BETWEEN-REAL-TIME-KINEMATICS-AND-PRECISE-POINT-POSITIONING.pdf)  
45. Ground Truth \- Professional Land Surveyors of Oregon, accessed March 1, 2026, [https://www.plso.org/Resources/Documents/MD%20Dennis%20Ground\_Truth\_handout\_v22\_PLSO\_2015\_rev1.pdf](https://www.plso.org/Resources/Documents/MD%20Dennis%20Ground_Truth_handout_v22_PLSO_2015_rev1.pdf)  
46. Grid Computations | PDF | Geodesy | Latitude \- Scribd, accessed March 1, 2026, [https://pt.scribd.com/document/755131577/GRID-COMPUTATIONS](https://pt.scribd.com/document/755131577/GRID-COMPUTATIONS)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAXCAYAAAA/ZK6/AAAAv0lEQVR4XmNgGHKAB12AEHiJLkAI/EcXwAcYgXgOuiA+UADEMuiC2AAzEFcB8TcgbgNiTlRpVHACiK8AsRwDxP3sQPwaiNcgKwIBVgaIgiIoH+T+2QhpsJwmEp/hLxC/QuLnALEsEh+k4RyMYwcVQAbY+IkwjjNUABncRmL3MmDKgwVUoWwNII6EstWgchJQPhyAFIEkkoF4JRBbAfEFIP6ArAgbANkC0uiAJo4XILufIFAH4ih0QXxgEbrAEAAALhYipB29itUAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAAhUlEQVR4XmNgGPrgPxA/AGIWNHGcAKQBhIkCExggijnQJXABkOKN6IK4AElOyWCAKFZGl8AFQIpvoQtiA+IMJDjlOhDfZYAoxhvmD4B4JRAzM0AUL0ORRQIvGVDdidMpH4D4O5pYIQNEsRSy4GeoIDYAEr8E48hABUBuxAb2MOA2aBQQBwC0ciJVn07c0AAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAZCAYAAADuWXTMAAAAzElEQVR4XmNgGAWRQLyFSIwBWIFYHIj/Q7EYEPMAMTcQiwKxORA/gsrhBCDJf+iCSACnZhMGiGQ/ugQSwKkZ5B+QpACSGAsQz0Pif0JiowCYf5HBZSCWRxPDCmCa0TFBYMYAUdiJJKYHFSMIyhkgCj3QxO8isYWBmBGJDwefGTBtAcW9FxL/JxIbBRDyHyih7EMXBAE2BojG0+gSSAAkD4o2DDCBASLphy4BBAEMEDkMJ68C4j8MkOSIHj0gDBL/DcTfgdgAqmcUDC0AACh/OzCQSURoAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAAA3UlEQVR4XmNgGAWkgnlA/BmI/0PxAhRZCPjLgJAHYWdUaVSArBAb2AfEKuiC6IARiLcD8XoGiEFBqNJggMsCFJAPxCZQNi5X/UEXwAbeIrE/MEAM4kMSUwPiTiQ+ToDsAlA4gPg3kcSWATEPEh8rAIXPZjQxdO9h8yoGQA4fZDGQ5m4o/xeSHE7wDl0ACmCu0gbiFjQ5rACXs3czQOTuATEnmhwGYAHiveiCUMDEgBlWWAEzEL8B4pPoEkjgGxB/RxdEBquA+CMDJP2A0g0oL2ED+kCcjS44CkYBEAAABi803bhnVOIAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAABRUlEQVR4Xu2UvUoDQRSFrxIEERJBxNJWiyBEfAF9AhsrwUIE8QVS6QvYWIrkHcRWwUIQRBT8t1IQewsFtVLP2bkjN5eZhZSB/eCQOd/szO7CZkQq+pkh5AT5RQ7dnGUTeUc+kVU3R3aRM+QLmXZzBS0JN2lon9PueUCOTL9DTk1fRkZM3zLjf7jxdcLdml5X56Eb1THfyDNly7iEBXtWgkv1kSvXI3QdHa8hNTO3YcYFKxIW7Dh/rD7Cce5m1h8g+8gTMm98waSk3+xF/Zh2v2kk57Pw4puEY/ix2O7J+SwLEhbw8ydtCR8H3aC63KY5X8qEhP/XPdJEnqV7k9ymOd8T3ODH9A91HrpHL8tIPR37oulL6jx0s16WwQU8fiIXyJvpEV63bvq2up6YkbDoVX95RqYYljB/LuHE+UYGuq6oqOgL/gC84V9iDl/IsgAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAYCAYAAAARfGZ1AAABC0lEQVR4XmNgGAVEAEYgVkUXpAZ4CsT/oZgm4AoDDQ0HGXwNXZBaAGR4BLogNUAUA2aQNAGxP5oYWeAmA8JwLiC+D8R8QPwNroICADL4NhALAvFGqNhPqDjFAGTITiCeiS5BKQBFIsjwq1B6D6o0ZeA6A6r3QewpSHyKAHr6BvFXQtkfoXQaEJ8BYhMgPgfEyxkgeniB+AIQvwNiY6haFAAyLAyNn80AKWuOQcXWAXEOEP+CKWKAqIuBsi2B+AaSHBiIMWCmCD+o2Ac0cVD5Y4XER9a3FIhrkPgkA2TDHIH4ERIf3YEkA2QDDgJxPJQNCj6YXCyUJgm4AHE/Ev83EhsEPjNAInYUDCAAADvTPw8mvgLOAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAAA7klEQVR4XmNgGDGAEYhV0QVJBU+B+D8UUwyuMFDJIJAh19AFyQEggyLQBUkFUQyY3moCYn80MYLgJgPCIC4gvg/EfED8Da6CSAAy5DYQCwLxRqjYT6g4SQCkYScQz0SXIAWAAhhk0FUovQdVmnhwnQHVCyD2FCQ+0QA9/YD4K6Hsj1A6EohPArEuEJ9jgISnNlQODkAaw9D42QyQvHcMKrYbiOOA+A5MEQNaRIihCwCBH1TsA5r4LSB2R+Kj6yMaIGvMA+I3SHySAHqEkAVAWegMA6S4+Q7E/KjSxIO7QOyFLkgqMGGAeMUQXWLwAgDjUTmdx0OVigAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAYCAYAAABnRtT+AAABxklEQVR4Xu2VPShGYRTHj5R8RCZSGMhClIlkMVkYfcwyKB+LlJQRG1lMSialRBnEpCgGJYOYvFlQkiyU8nH+73MeznPeexnd8v7q3/uc///c933uvefelyhLlj+l0RpJZNkaSWOEVWXNpPFgjSTyYQ1LLmuRdc86ZDWEcZpu1hVrg6IHvIa1wzpnDbGOwziWNtYK64bcb0TSSu4sOqQelLrsq4PolTWt6mvWkaq7WBeqrqffr0w7uZ5J1jirgtUnXonqSwPzQNW94nlSrHdVe9DTKWvcgTWVgZ82uUlhrudxivWmauon14xLHgfyBWuS8/0Pzcn6kTXByvNNEbSQ6y1Unt4wxiY4wW0xcrSpqCaXz9iAwk2CXeVBWyrTYHSCTZCbSc8YmXxWjFptGpCvWpPCTer5zWedSlaqfA/8fVXjIdPvx2dRAA5aNx6uLE4AIMdttMDfU2tsTgMvaoxeWCeqvlXrJnLHZdzZeQn0a+eM3GsJ1FFmviSeB+uUqr0XRTm5rFhq3zcgaz2rAXhK0QA9sQrCmIpYl/TdY/9j4TXLJ4S3AU4uDjxY+vswpz1BR4IYZlVaM2ncWSOJxM1tohi1RpZ/zSdlmHPxv/dT5wAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAYCAYAAACIhL/AAAABw0lEQVR4Xu2VPSiFYRTH/ygkHymSr4GsbCIZFGVik1FZyFdKSRYDm1FhUNdgwWCWwWVQyiIlRSb5GAwoosQ573Pe+57nee+9THrL/dW/e87/f+77dZ/nvUCGDH9Ko2tEjTXXiBJjpFrXjBKPrhE1vlxDU0TaJF2TpkkbduwxQLonrZPy7ciDj8HfeyDtksrsOCVtpBjpltTjZB41pDfVlyJ8N5+kFakrYPKGIMaQeHXS84W6x3Bph5mZIU2RKkn94hWrOWyTrrRBPKn6FOGTaS9P6oUgxrJ4qdiBnev1NwvzQBJ0wwy/k+ZhnqCGs0uYJ+drTnxmVeos6X+iBWa+QHn6Yuud3mNRTF/nKuP+jNSVRMyLzPyWD4TnY6qegJOXqDqbtAUz0CEe1zf+QBKOED5hOng2rvph2O+/V1GCfVKrNmDuktcCk+oJHcpnIUw+ojKmitTreAxvyBPV36m6CeZY1nKJw97FDA+VS50j/UEQo5q0p3q+SZ7Ru+9Z1Rr/LcCvJca/+UGp9dr0iJOaYTYJD7A69YBwjCBfcjJmEkGebkkwuaQLBPP8i/VZExFhFOY9HFn4nynS+Osvsoy7RoZ/xzf8LXBvhaP3GwAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAXCAYAAADduLXGAAAAoElEQVR4XmNgGJSAEYhV0QWxgadA/B+KiQJXGEhQDFJ4DV0QFwApjkAXxAaiGDCd0ATE/mhiYHCTAaGYC4jvAzEfEH+Dq0ACIIW3gVgQiDdCxX5CxTEASHAnEM9El0AHMxgQJsyGslUQ0qgAPTJA7INQdj6SOBiAJKeh8VuQ2HDACRUQRRL7CMQbgLgHiA2RxMHAE10ACDyAmANdcBTAAACQdCSKrBERiwAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAYCAYAAAAMAljuAAACx0lEQVR4Xu2YS6iNURTHF13PEBEhA0khGVwmzJRumTCT5DFiQhlgZsQIAxO3vKJ7Jd3BVSZKmZgYSQaeUcojr4gUIY/1b619zjrrPL7vu53H3vl+9e/svdb+zlnft/ba3z6bqKSkpCRZxrGWemMiTGet9saUec36q0qJyayvJHH/cb6YWcZ6542e+5ReQgKI+5Q3RsYA6wNVJ/77Wnc9GPTQGxNgHkns+EyF3AnZ6o0dYD5rvDc6NnpDC85QepWdmZBtVH9TR1ibna1d4Lf6vFH5yZrqjS3w774ZrEusacYWG5kJeULVm8LDeE5yY98qI9oPfm+Cs/2i4g8S34MqAZhEh1g7Wb8rI+IjMyEY8JQ1i3VNbT/U3klsUpAMbF+LgOUP37GQJCmL1A7bozBoDKwiqbJGGmYNsS6yLrDOs87JZblBfHjBNwUDblB1pnUT/DaSgYosymmS61Hhs419imnHCGL+6I0BvMgx4IF+3qx1dxz8f4AmeUcOEC8UqnlTrTtaEOsnbwygtO3ShHa39vRIRHhnoD3R+PKAWAe1vVv77WAx63hBFQFxfvbGAJz2/wf6I9r+op97WHdYa1h3WVdIrsGaf48k20WPLmwyrM2/6JsxhyTWudpfrv0A/uiCZ2pfSfJ+fFUZ0TsQT3i2dcC5xfX3kpxt3VbbVdY+ki1pAOO2a3st67HxZYEdULOtLZLSbEtsOUG1CcCsDv2jrJmsBSTHK7D3q+8A66C2ewXi+e6NALPLlznW4UYlhfOudaZvr7vMOmz6rVhC2UvTDm9oACrTnyyE459jzm5jHSWZYN0GFYqVBM/xpeoNyVncmLA3tZ71wvR9UmMCVYJdXACx2omVLPah32Lt0jaWtuDLM7O7zVmqVgSS89b4kmUD66Tp2xkHUHZYQmIEk2U/ySS67nwlPSDm5fS/A7tFJGSFd5SUlKTGP/9TtPuFx606AAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAABJElEQVR4Xu2UwUoCURSGDxUkJETQsvb5GrnxAVpJtnNRYRS4za0b1+IbtGgRbnqCjF4ghKhN6kJa1CYKEeo/3dtw5lebmVol88HHeP//nrkOyoikzANVuM+h5wWW4BpchTvwObRDpAVv4BvMUffFGRzBD+9BuA747q0bpt+FK2ZdM5+nEnVYHTZhnjpFn4jZ4sASddhPlOGSWc+6T8BfDlPa8AI+wG3qJog67A7ewms4lvCTJEZveMihR7tls7702a/R4QqHM9AfX/efchEXHT7i0LNI6wVx+7uUx0aHjzkE9+K6jMmyPrsyWSJ0+IRD8AhfKSuI21+kPBbr4oYbXIBNcX9ny7u411IizuET7MOevw7FvcIse+K+zMBfO+E6JeW/8AmpPUYCuCy6cwAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAXCAYAAAA/ZK6/AAAAlUlEQVR4XmNgGAWDCegC8Twg5obyeYG4AYgnADETVAwO2IF4KxBHA/F/IG4G4gVQuXqoGArYC6VhGhqR5EA2YWgohdLXGDAls7GIwQFIoh2L2GU0MTCQYIBIgpwAA3xQMQUofypCCsJBtxpZrBqIlZDkGP4C8VdkASAoYIBo0AfiS2hyDBZAzIouyACJHwN0wVFACAAA3qgdBAlcrcAAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAYCAYAAAACqyaBAAABbElEQVR4Xu2WvS4FURDHRxAfUdGIoBUP4Am8gcYTSEgQUdyEVqISvY/CA4hChFapUmnR+uokKHzN38xxZ+fek7tnT0Fxf8k/OfOfc+bszu7ZLFGbf8iANxKZ9EYK995I5Jj1xZr2iTJgYS6o8enNVnSw9r1ZgROqcBMrrFFvVqCPZPNtn2hGJ2ud9cLaJFmcCzZvefcXrCvWOMnkHtYj69BOqsAWSb1+nwDdJMlVjfG89+rpn1zWsSGpcepN8MF6MPEia8zEWHhp4lRC2xtaP6TmiPHuzBggv+O8smDtFGtBxxM2OaumxcaDGuM9SAGPDuuWjIf4xsS/xS27ZvzGOjMxqLG6nGfBiUHNI+c/qV/glnWu43nWMMmV400/UD+wTFLg2fmBsPG1T5C0H7kZn1jTRBC+y72FGXVwse/eVHBK0K0YryQveFMa2hKh7Lwk7PmOgY9PmXlJzFHxyMWIti2HDW9EyP3JaPN3fAMvU02KvKhFFwAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAYCAYAAACMcW/9AAABqElEQVR4Xu2VzytFURDHx89EWZCNP0BKSllgqSxkIXtlZS1FZKNsWNhY8D9gYyEWFoqtlbKVjbIQ8qMkP2fMGebOO6d77vPSe3U/9e3Nne+5M/ece949ADk5lcUB6jNSxXCNeodwjSNI9rhK2oWEChHtEPZimEYdA9dYMJ7wZhM+aoCLnFpD8ZcHvXG/ocXoRq3apI9Z4AKjJk8rIfgaxCL3nrm4S3nEJqrZ5LzcQ+GDjKAm1HWfirNQhdp1cRNwn8df+xvbO4i8kgHUIGrOXZeCKVSvuv4Ark0TEF5VHET25wVqGbWOunS5UiD7UxgGri2r3AncN5V54BupgOZcxa2QXIEs+CYsb5DYAt4SqdB+scXqgPeo8KLiLFSj9mwS2QDuOel+o9Cz89GGOrTJSGZQ/TbpkL5Ri1APPPjEGgrya20SWbQJDw82oaD/BNVesoaPNeDB9vtJjEF4xjvA3r41FEPAYxqt4WgB9husodkGPrLkU2FFefpkPKN63D0aakJnOI318YS6Q926eCVp/0Dev0AHRdnTgRq3yXKEtkdFUOwBkJOTxhcO0nWCRyq8fQAAAABJRU5ErkJggg==>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAYCAYAAAAs7gcTAAAAf0lEQVR4XmNgGAX0BtJAvAyIc9ElgMAWmXMMiP8j4TfIkkBwA8bIA+K3QMwK5UsyQDTIQvkLgZgNygZLoAMHID4AZYMMIghAhmQBsQi6BDYAcz9R4D0Q16AL4gJP0AXwAaKdwATEr9AFcYE6IO5GF8QF3gExH7ogLvAbXWAQAQAYqBfQoq3vPwAAAABJRU5ErkJggg==>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAYCAYAAABurXSEAAABKElEQVR4Xu2WPUoDURSFT0QETSFkCRLsREIsLFxBQPdhERBxCXZq5TYCqVJZJpWFW3AD/hRCUPy9xzvi8zADb8A3Fr4PDsw79zy4zNx5M0Amk/lt3mtoVuz5wdx0qWZC1k3PpuXA68EbPA88cm06Eu8Thg/UTMiVaUW8MbyPjvgnpjXxsAkPL2ghIW9q4HsUlGm42DENTBfw8G6xboINNeA9vKpp7IeLQ/isMHxbrKm/oA/v40wLVTA8VLNhJvA+VrVQBh8Twy0tlLBk2ooU71wdqua5lBHiw23TXqT4ftSBPbyoWQXDd2o2zDa8Dx5tUTAcHtylX57EfJ1eUfNMGO4W109hoUFqzTM5hW94NC1KLSU8jx/go3ljuof/StA/DnKZTCbzX/kAZSFLYFN9JQkAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGoAAAAYCAYAAAASy2hdAAADjUlEQVR4Xu2YWchNURTHl5kHQ4gkJaWEFC/KHB4U8eRNGTPmM4QHJEmGePHAiyQpQ4YUEUWeZEzJPH23TJkfJGVe//be966zvr3PcLuf3Nq/+nfP/q99pj2sve8hikQikUgd8FMbGfTRRh3QVxv1xgXWH9YJHQjQinWfzDm9VawaupO51hgdqCEDWTO0WW+gkZyKgPpPtVkFu8hc66IO1JDj2qg3TrEmkGkkNNbBZDiVT1S8c0MM1kaNqdVzptKFNUSbHpBCiiJfoOisGkWm/lQd+A/JnPnI4YdYS3WAGa0ND1/INMZ7+3smGU6QFvOB2TNZlK+Succe4WWB+t+06aEf6xzrHmshmXuBNqz5rJ2sTdYDs1hbqJKyBrH2sla4CjnB+yFr3GKNVLEyVyiZ/z8kw/RQlTWnWT2Vt4z8o/gsa5jysvDNnqKz6iZl15/CeiDKWNjdOR3JdADKl8o1iDZbDyqRqdfCljF4s5jJ+sWaTaYdwTrr4TplGlgfyYwY0IvMTdy29gCrrT0OcU0bgkZKDoLDyXAmmDXTtcncIXO97ToQABkD9dfogADZQD+f7lzdUeCl9dsLDzNKn6t5RMnOlPWxwy2Jsvdi41iX7TE6MYtEzweQL1EE3/OBllTp/CwwCOVgCbGVTPwzazX5B6ivo0rWlyzyeJJV1DT+TBzPoaZxL6i0mPIv/COo0hCPqTJDfegXDbGNTEoIgYUX91uvA4IOZOp0ZR21x+jkEOcp2alYNyS+jnLPIZnn8SSunRwDyKRBx0lKP7+Me9A8TGJdp8rMwqKLc5E2Nd1YK7UZIOv+cqb46EwmNtyWW9vy/nKNJD3EMTLAbTL1sZt1+DrqifUlcz2eBLGNonxEHAPE7yrPC6Z/2kiV/NCGBesHboi8P561z5bzsJb8O1DNGzLX1HXR6PCXKz+tY+HrFA0P2UKWdUeVrC/JM6Owg5RlxwJVTgULZF6WaEOB7WuJtVv5abgGLSIHdqAo67QFsPYgJmePA36jx9PlG8pzf0kkGGjwQksAPkMh7rKQ21ljcH+3x7nQN/6X4FuX7oQ8moaTyaSi5/bYB+q+1iYZf6j9hX6z+tvYRDIdggGMc79aH5steC9Yb2097OReWQ8zHjs4HxhQOMfdD1ms0HdELLbvtBlpNo5pIy8bWDu0GWk2MJuqAh8xO2kz0mzgj29VhHZxkdrTjjVWm5FIJBKhv6ceDp3LloNgAAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAYCAYAAAALQIb7AAABGUlEQVR4Xu2TvWoCURCFRwKCPkRa8QHS2NpYW+QFrCwC1oKVjaBoIVYpgg9gihBS5QV8AEvt7NKbFP7MMPfC7Mk6uzZpsh8c2HvOmd17d1migj/gh1VB06GORl76rDNrj4HDG+lME4MsZCiqDJmH9E9oevRYQ9aAdHiXjF3eSWdyY8vxdHfG85BvLP0pBml0WGOzHpEOb4yXRdxgJmml3MOBCWm/ioHlkbVAk5mTDq8xcJD+B5oWb/e3nC52r/ZbrCWahhfS4U8MAOk8sLrhupaMlau7MHi7LZFmT8aT9a/fpsFaoZnCK+kNsCu/hfiSW76Cn8C+47yKxAdtjReR1ylZOxr3wbhVMxlmnlnf4TqNA+uIZkHBP+ICWA5di9ED81QAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARUAAAAUCAYAAACjxanzAAAIHElEQVR4Xu2aZ4glRRCAS089MUfM3poxxx/mhOkUcxb1Fk/MOZ559cAcDgNmeWbMiooBEUVFRTEdmFEU85lz1v6uu3w19WZe2H3nLrf9QbFTVf16eqZ6arprViSTyWQymUwmk8lkhg1ne8MwZtcgzznb6CA/BPnHyOdBHguylmnXDn1B/pLYx0C5XBpjt1mQL6Q7/ZdxlsS+d/OOCo4L8kuQe72jBWVxaAXjWsYb26A/5+I+fxXkS+8wHCPVcfgzyJzOdkCQn6X6N1UQ760k/m4H5xs0Or2IqZ2q+4F9grO9luwbO3sz7pfGcyzr9Hbx/cDqUm7vFp0kFfg9yK3e2AadXsNR3tABnZ4LHpbmSWWGILt7Y2KLIK97Y+Bo6WwsJO2T0zFxn8/4BpVvpH8ZfmqFybKfN0oM9jneGHhaom9p76igJsWJMyLIj0bvhLLY9UhnE7NTOk0q3wW5wRvboCoOU4L+nItE2SyptKIsRr1Sbq/ijSAHOdvjTh8UeEuW3Zzpg5wocdAce/YOcmeQsd4hdduqQQ4z9qWCjAsyo7HBYunvTEGODzKv8R0RZBWjK2To24Ns7h0DZDopD2xVUgF8fzgbYz4jyALOXpN6/9OmY7YI2wcZmezc7wuCXBpkoWQroyx2PdI4/rmDXCZxu8Q9tsyR/pLcDpXiqokHbQOjgyYVfnd+kHWL7sksGeQKiSs4ksr1RXdbsauKwy5BrpO49ZzN2JlTyxud8a2ZjpmDvMmrqDrXCenvSUFOsQ4pJhXmaNlz4O+d5bYgxzpbr5SPg/u9j7NtJ7HtlRLnDvPs6mRDRwYVfyHs99gzwjwS/UwCbh5QU9gkHbMnRYc9pb4vfFViIOkHeSHINkGuSn7lgaTfFWQvicFDXz/IhUG2TPoe+oOkK2Rrm7gsKwXZqYksV29agD2vnbDAOauSyt9SHBMrCAW7nZC1ZFOeCjLJ6PNL0c9xWVJXfOx6nI04/WR06+PhROflcbjUJzX35UaJCQOdmCno10qsKd2T9BeNH9vWRsdfc7rSLHbg43BTkCXSMWPTlw0vPvplfsH+Sb9EYjJlPOhrJH8Z9lzUKLSORr2FueJrYSQV5vUzEhPx9xLrG7BekOelMTYe7+91Nq6VxA1smfBNU3dP1v22z/c5aJwb5GKjfyIxGAoD1YsDJunM6ZgLtxcy3ulzOR3Q9Q2pugWdBKO8FOQVo9v2TP73jW5h1fNmEzmk3rQAiYx6iYVzViWVh6Q+JtroGxJYzdnx1pxOUtGkDCRiu/qg7Rije3zseqTY/8ESl/cKvlEtdJKGQmK3/fnx7JxswMvItgVWcCQvxfqbxQ58HPgtLy7FFsrxaVJR/Tyjk/j9isniz3WNNF4LOvcDSCrWz8rA6gs6vQxWqLYO0iuN99qC7mM5ZJMK2ME8G+Rto/MA8jbzsFy+WYq/7XM6lOm2FlDmt0mFN9SnRldqQV6WuMTuNmVjqkoqb0m9PX9ZZXlRaqmNQlIpuzaSLm9B2h7pfB7bX4/TFbaYvHXxsS1V0EcZ/WspJpV9pdgfx7w1Ldh4O98RZKLzERvbn1KT9mJnzz0m6XZuKtibJZWPpXW9wZ5LtxIWal/EGnxSWcTpbEf87z1rB3nP6L3SeK/9POI+W/+QTiqsTnQ5yR6cwWk9gKWfZZ0g76bjxaV4IX1OhzK9k6TCG80+eAT09HRMEbDVxOwPPCC63QPGVJVU8P1mjjcyPk9NitdLUuHeW76VWH8C2rZKKjZ2PdJ4P4nfLOkYX7OkwhLeJoGxUuyP47KkQjzZAvhrITa89ZVOY+fjsILE8yErGjv6QJOKPVdZUuHl+kg67kZSAdum1+hlqz4P/iGdVBaVOCkUlvRsbUYam2IH/n8nFf/JtNnEpNhJ2yrp+69lI+xd7Xk4Lksqup+fPenszW1NBSjIahGxJsV+SSpMeIVPzrZGQdtWScXGrkeK/TMWu3XFNyWSCvBQ2rZAbLQm00nsFBuHccZOjc6Pa6BJxZ6rLKmgay2xW0mF85yajnul8Zo2NDrw/y8K/iGdVEAHREWZvfisxqeMkNhudNLZ49kLOdPpUKav7HQLun5/ByrlLMuBijx+/g+Aqj31Hf/7bvGrxEI1cA4KfxYeCuz2ISURY3tC4viYbDZpcC12vPSpOl9LKHTrylD35SRH/8XMo31QNLT9c/xZOtaHmsKl9oduEzxJkSKscqA09mcLsfzTlk22+EmMVtf/yehv7DQOti1vcv4HRsFn6y3oE4xO4ZXiaSv0XD6p8EWSe6M8KEU/xW2r8y8G7VwbaDt/r99JOoVjIIFsWndP9o03uto4ty3oDio8yCxVeUgYnBflvqRrgZC34S0SP/dp2z6JgeDNh67/tahvM/anLNm1Sk79gIlOMU374LMZXwdUJ9kBVXd0brZu1Th3t+ELAwmBrY29D5MkjnfbetMCJFxty1czhaKq2jVBaZLWB59ait4fjvmsS6Kxhe0yiB1Lcx2rFvTYIqB/JHHFxKqBwjCTTmPxgcRkeFHSESYwxUseJHTaAgmIrzYUk4mD3eMD8aAAyW9YKbAS4QWl9Cd2xIE6CsLLhe3Th8ZPEqMfisI7Sr04jjCHNHEjrLyaoefSpMJHAh5uu3ock3wIfS8sMV7o3BtWTCQx9CfTb5rBPTpN6n2yMlc4r9pXM/a7jZ24KY8mW7Mt+KAw0RskTn4ClMkMB/xKJTMAWNr6wizYLxiZzNROTipdRpfQLH0pkCLsgTOZ4YJu0zKZTCaTyWQymUwmkynjX3Y/sPWfv/g/AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHQAAAAYCAYAAAArrNkGAAADyklEQVR4Xu2ZachMURjHH4QihI/ilZR9yZYsecsXkiTKrkGULCF8sVPIviRkyVLCB8oXZHvLkmwlspTI9sn2QSL7859zzjvPfebMa+bONPeW+6t/c57/c++5Z+bce5Y7RAn/NX1Zv1g/WZXBVKxpwfrG+sOapnJRcZtMe67rRLloyholYjSmi4jjRkdWQ1veKXy0e6aIo+C9KB9h/RBx2ZhM5sdwfGXdEXHcQFvfsVrZsuO8iqMA119vy7VsHIae2igGNGKTNmNErhHkM8XrRuxN4Tv0mTbCguEsbCPKwQjyt68++f0owXA7Xpt50Jk1SZth+a6NmHGXtUubZDoTQ1xcOMAaq808Oa2NsHwQ5VOiHCd8T+EnUS7ZUFUEU8nsGkB/mcgT33espjtrL2VWhY1YK1nbWLWtBzD/pFhTWHNZS0QuKiawTrK6Ck92HnhMps3QLNaFYNrLGNYb1iPWQpUDzVlnWA/I/BY+trDesnawhrIqrN+LzKIoxZrOemr9fOjA2k1m6zhR5dLUY11ljSbT62tYh2xuhfXAAluW8i06ysVRMm3oZuMq1sjqbIYelN3uOYEjssG8dlPEOAf7Rsd+1hcRY9jUT4wvRme4sta/aM36zdpKZnU7jtWPzLntMocRXbGf2JshuUrk8KTmc7Ga2Efmx/fpMJmb5yCZ+QTHDkufVTNnKbtd2COvVV4YHlJ23Yg32zJuYp0HeBLddNSJso+ZT5kOLZRFZOqra2M5f7pOrWaZ/XyuE8wMjxc1dci0yS16ME0sJbMvLgWoG2+VcoE3Zb7fZDkFfZQh3LRyOiiUJmTqwfbGoa+PuLHy0uYN5eGu0ydHzUYybdpDZnpIsRrIA4oEdV/SpsB1lGYeGR9PDMCw6I6FcCOE4R5lX++FKONm0fk0MId4vIvKK5TVrA0FaLg5LSeXKccXKBGo+7U2Bbk6FMM9/JZktkZye5SyuSrh5QvOk9vE9hTcf2Kuz2qPb1IH8AZoM2IwvPraCgZrIwRYyfvqx0oZYFHiy+Ptk/MHsc6JHNhO4aaFWxS83nFRdsNxM+GlwdJbNxL7JO3FBbSrjYjxNHwksxIsFvwJgfqx8ndgpYwOcWCOlatebGFwjpvnKm3stoEACzlMEYXi1gxtbez6ZKAtV9g4APY08h8J8JLi26G4M7GER/ugY8F0SXhFmfoXqxxwQyyEtQY61VHJWse6L45BXAzXKFMXNDuY/jc4Cf9MJMQHbIe8LxPyAR3aR5sJkXJCG/mSa5GUEC2h+wTvLp9oMyFy8MoxISEhISEe/AWNJv3rQW73GAAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAAAn0lEQVR4XmNgGMyABYgN0QWJAWeA+D+6IDEApGktuiAxAKSRCV2QEPAF4t/ogsSA00DsgS6IDryBeD0Q2yOJ4Q2UGgaIAkcovwOIJyKksQOYJmTPCwPxMSQ+VgDSdBXKZgXiNKgYXgDyEyyO2oA4gwFiG0FQx0CE6diADQNujTHoAugApDEJTQzkZ3c0MQwACs0fDBADQHgvqvQoGOQAAEV+HehcheHTAAAAAElFTkSuQmCC>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAYCAYAAAAMAljuAAADoUlEQVR4Xu2ZWahNURjHP7MQQkkSRSFSiAeSG5klDyRT5yYpc5Eo4kGJPHgyJEPm4cWYFyXK/KC8SerKEJnnOXz/vm/dvfZ39j57X7rnnH07v/p31vdfa++z1/nWXmvtfYiyw27WH9Z31gj1nqt31jWqUFyOkCTA8dErVygRSEhrkrujQhmAKcu/S7LMYGtkkdPUcBLywBpZYzWrM0lCcqYuDResUUL6s+ZaM0tMZg3Usl3c0/Ivx9QXp6xRH7RnDbBmBJ2skcBYyr8j3OKelsZUXglJvJaurKOspbaCgn1/IbAFxZe81M/z4eoQhep8hrA+sz6xvnr+N/VQd8vz48A094vkuiaqkGSfWSTPMzWsbaYOzGCtYx3SGINvA2tzbYt09GXtJLmeOaauluskF+v0KlxN90xsOUfSaZ/lJOeaYnzM44OMV9+sYB0guR6UoSVe/X6ta6rxDo1xVznWkAwE+EjCaPUvqpdED9ZvkmRjdzWTNYzk2N5BM6JlrNesZhp3IWnUTWN0pLmW4yg0SjHi/GQfC1cXjekU/8NhVrB1iDFQfearv9D48IYaz2cVSRv3G/vrh0tKLfZCQBXrspaRrCQaWSOCltYoMoUSYmlF0vad8avVt8Abb02lHUk9pl+HPQfitsbLA40WUfoF2GUauk/BaIjikjVicOeri+JISoh7V4a7Iqfl96EWMudHnQPeBGsqdyj/mBqvjE2QrY8kqYM+GB23KbhTFpAci+nO0pFkDi820yjcnxteGXeC7SviD8abrb4FHjYKUaDuhxf3ofDzx02KPmceb0l2FWn4aQ1lC8mXYd0YxdqrcSmYSuHvRv8c8A96sfOwc+zBmqdetfoWeJOsqWCg+scc98puOuvgebE8sUYBFlvDsIn1kLXd+HUBm4xdJB3A5z7WI0reATqwg8KxwzX2t9Hwn3lxjmSQwa+iYDpaqZ6/yXHrDY6JoglJfS+NXXLwKIFyd40TiRoJpQYLo70uxIeNF8d6kvaQ/1DZhoLnKAijHWsgkuL+a8Fzz1PWY5LkXWHd1TI81OG5KI6rFJwf8rfdiWD//cKaZcAZ1jXjoXNpp9ZS048KPAwWAiNpqzXLAPz4Y7x4I8kuJiucsEZa3lCKfXEJQEJOUvAKvme4uuyx021q4nZNpQRvev0OtTBxFthjjSyD92X+q4yRlL2ENCjw44/zYkxdLiF1feNa4T/AW9UvJNtSfObUxxqHhKwluVsaBH8B/zj4LChjjjQAAAAASUVORK5CYII=>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAXCAYAAAAGAx/kAAAAp0lEQVR4XmNgGAWkgmgg/gnE/5HwGyT5X2hyt5HksAI3BojCp2ji3ED8D4i50MTxApit6GIkg5UMEI3NUD6IzYyQJh4wMiBc9Q2IBVClSQO/GSAG2aNLkApOMkAMuocuQQqYBcTlDNgDnWjwF4hZoWxnBohBdxDSxIHPQCyKJkayq54AsQm6IAMiKdSgSyCDFgbUpP8SVZphLZIcCJ8D4kIUFaNgpAMAXYMxGjJZzX0AAAAASUVORK5CYII=>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAYCAYAAAAlBadpAAAAy0lEQVR4Xu2SMQ8BURCER6XSqiVahd8gWr3/4g8olCqVH6KlUGkQnUonR0hEEGaz7708e+/UivuSSS4zs5fbzQElI+pMvZ1u1JF6RF7Dl4vwRcsM6jdtECOFuTVJB5qtbeDpQwtdG5AJNJsaP7BB+pOFonUCqUKbelJ74+eQQbnwklpRd+dV41IKv68cJmbr/J/skC4NoX7dBjGpfYUr1K/YIEYKC2ui+KWBAbTQswHyw+F5TF2oDHrlE/XyoaMFHThA//fad1zy53wAhPQ9J2j9tisAAAAASUVORK5CYII=>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAYCAYAAAAYl8YPAAAA/klEQVR4Xu2QsQpBYRTHT1JEUgYZlIXBYvAAFguTweIFZGCySBlkMshkNSiU0eIlbN7A5AlEBpzjO9+9xynDvRnvr/7de37/z8n9AAKYDCarpVdWmBenrzpfFMEsC+vCDzswy/4CLbpq6YUZZsLvtGwkOkkPs8SUdEEMMQ9+L4B7+RHnhCHGPsHzHlNxa4A2mANR4U7sNHfMVMx0pi7mj7hIwe6mHGH/8RyTVB3UwJQd5cmNlSNa4C6kHGW5ZSnJs5OfrSmDueOv3y60QNbCbYQndxBzjp1DXIkmz9bZZxrMHYZ4Js6Yrpg/VMFdYMsnzyl7CBmwo1DfEF1AwC/exiJAFJWoA94AAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAYCAYAAAARfGZ1AAABO0lEQVR4Xu2UvytGYRTHDynKyyCDwcjwLjLKyGKwWYwWDG8ZTMggMyZlVihmZfEf2JRsFoMsBiWl/DjH8z3uud/3uQaT4X7q232ezzn3ebr39lyRmj8ypBlmGZjQHGimgtsP4yyHmk9klWqGbWq1DU23ZhbzY81F6KukKemGLvKd8IPkB+AnyWc5ldTM3GmeWYJcfxZrfGEpyT+yBL8uvqPZxtgaN0PN8W+xQL6Sdc0bxqNSLGAfi7mSou5ZK3UEFiU19AR3DVfFrrRvcFbqAFZ4yLhXclUsSbFBiRnIZfLmtsg1NGPknHvJLH6SkSNw8TUZe5pxcs65tK/zfVRZHgVnJ85516yEecT651n2ouDMYe4u1tx3BGfcaG7J/TAtxY0tuA/M7Ugb/ZpLTZ+kJ7DaE672f6mp+a98AaOtVZz4s6WEAAAAAElFTkSuQmCC>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF0AAAAYCAYAAACY5PEcAAACxUlEQVR4Xu2YS6hOURTHl7e8BrpCGXmVZwaKZMTEwEAYyIgBkpKMvEJuUfKYCCHyLDK8dScGDIxuXVKYIEWJgQF5JK/1v3utb6+7zvm6537fuedM9q/+nb3/a39777PPd9a390eUSCQStTGNNcObhuWsC6xVxjtnylUzkjXfm0PMKNZCb7bCddY/0V4XA3gYiB1gjWGtlfptVrdpVyWfKM65Kr5SyWPOo9AZvj2W4eJ3OH+y+CucXyV/qcQFKAjGw+KXwl3Kv4E3rC/eFPLaVwnGP+/NIQZj7vdmq6Czb96k4H/0plDnok+nMD5SX1Xg9wNjjvaBwXCKdUzK6OyQiSnwoS3Or5tLlH3oZ1lLndcuKylkAfR7j7JjKssozGm7Dyh4PX5JeQ7FhcWPpKeHYly1r1+LetC5gFmsR6yZxisD9LVHyk+k/j2GG7ygmObGsn6bWB/bKHwYQeWZeM04TdmFx1Mvws0mukFh13SNdZV1hXVZPlMEzAHtl1DMsfZBtAv6eZ3jHXYetpB2zMeu3geMDzneD+c1A69PmTfXCprP77O2uthAFJl7J2XbzBXPZwOkHfjYcGArnWENhQY7nA/vqPMmsBY7T3lH2UlVyUUK47+XK+pFKbLoeW1wJvGeoltX1QgbvCOmZbZ4Nt2AMxRe3Ty6KNtPM04OUkWwizJOyhtjuG3QX142+Ok8MEyuON9gU4J2eAMb4MjuF+uW8fA0lT+s3aZuQftN3qwQjG/356jvNOV2QR8Hczzd6b2V61PxLaivt8Z4MZUNUlfPxtTXJ6k8Z710XpVMojCvqcZDfQFrCuu48VvlM+uVqWOnhzEWsTZTzADwTmgjiqf6DKspLugu8TQn4WgPcGMPWBMpfOMRw0Rwxf8vdbKOsjd2RDz8mJUF0gv61DSDMw3qvY0WARwcdT0f9g8lEolEIpFIJBID8h9F49BVUbetFgAAAABJRU5ErkJggg==>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAAA/0lEQVR4XmNgGDGAEYhV0QVJBU+B+D8UUwyuMFDJIJAh19AFyQEggyLQBUkFUQyY3moCYn80MYLgJgPCIC4gvg/EfED8Da6CSAAy5DYQCwLxRqjYT6g4SQCkYScQz0SXQALuDJBk8haI2dHkwAAUwCCDrkLpPajSYADy5nUkPlaXghQgS4DYU5D4IHAWiJOR+CA1Ckh8uCBy+gHxV0LZH5HEfKFsEAB5rxSJDwYgRWFo/GwGSN47hiTmCVfBwPASiGcg8RnEGDD96wcV+4AkBuL7IPFBLqpC4hMNHjGghtE/IHZC4hMN7IB4GxIf3RckgbVAvJ0B4mUbNLlRQAAAAFjAPPcaGgN2AAAAAElFTkSuQmCC>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAAAUCAYAAAATMxqtAAACaElEQVR4Xu2Yz4tOURjHH/ldiIUsjB8JGQuFbGREiFKilIW9sjC7KQuJkr0QpXSzmxpFxB+g1MzKShaammgailIK+fn9zjnH+9znvef+cF8lcz717T3P9znnnnuf+957zvuKJBKJGcZt6Ce00iZ6xCLonrg52rAPeg1dh56anOYbtMx4F6Dv0vwcJqGT4satM7lS/mZBA00vRtMP/VDxDuidijWHoOfWBA+k2Tk8gnb59nForspV8q8XlGOHCrzFxgsUzZVJsR+DfTcbb8rEUXRBDyg1uisV6IvRc9SBY1cXeI+NFxiW7huQSXdB50CnoBPKmw8dFdd3EDomrg5j3mO8/3fvCLqgB6EzKmfh179MMfTFXIL2qriMhdJdCPIV+mJNhR2TGe+wuMKRiyZHGG9T8Wzv1SIUlHd1g8lZXlQoRjiZEXELVV22SvGFvJFiP/AJWqHiTPL97VjGZ03cqqBPoLs20UM4BwvOx6gJs6T4QrhqUzF2QuMqzqRznLXQZ2i30RafJ60Lut5/Dphcr+CxN/rP5SZXBccsLfDuGM+iC5CpmO/BquK0Ligfeb4D2Z6XT+dgvkwxQu6aatflI3TaeDxG1Y25BZ337Uw68y7wbbtf5X45wHyrgvb59qiPe40+5ntx77i6rJH8470JeqviMsK8XPn1OXBRY7zdxzckv3Vkjj8mNPS44se2a9NwA8uOH6A90DkfU3br8SfwW/RM3PFeiivOFR9TRzpdS+G4CeghdN/kyuB13ZTOfFdVjr+8gh8WsCXifonR40287H3yyvurlJf43+Hqyv1kTPyvIZFIJBIzgF89gLUV+JBtVgAAAABJRU5ErkJggg==>

[image31]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAYCAYAAAD+vg1LAAABJklEQVR4XmNgGAU4ACMQq6ILUgqeAvF/KKY6uMJAI4NBhl5DF6QGABkcgS5IKYhiwAyGJiD2RxMjGdxkQBjMBcT3gZgPiL/BVZAJQIbeBmJBIN4IFfsJFacIgAzYCcQz0SXQwEkGiE/QASi5YgBQhIEMvgql96BKo4BWdAEoaEAXAIHrDKheBrGnIPHJBujpF8RfCWV/hNLyQLwPiOdC+TCwCojPAHE4mjgYgAwKQ+NnM0DKjmNQMVDECgHxX5giIIhlgKgxB+K3SOJgIMaAGfN+ULEPaOKgiMOWgdYBcSm6ICkA3QEwABJnQRckFjgwQIKDF4gFUKVwWkg0+AHEy9HEDBgwg4wiAHI5CGwG4lxkCUoByPug2uYXugSlAFRQyaIL0hwAAHMaPZUCGb0JAAAAAElFTkSuQmCC>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAAAnCAYAAAAWwETtAAAHIUlEQVR4Xu2dZ6jlRBTHj11XXSygCJZnQ1iwobB+ERXBXhDXCoIf/GRHEURBLKhg76Kia68oiIjYFcFece0NLAiWteHay/nvZPZNzksy5U4mc+/ODw733jPJzEky/5dpySMqFAp9si3by9JZKBT65wy2q6kIsFAYjLOoCLBQGIylToD/Ceubzdkek85CNnzOtpp0tiDrzsH15CAgwFekc5JJITrNpmzfSmchO/5mmyWdFq6lZgEuy/Zbh50yveliIMDXhG+iSSnAlGUVwlmJ/K9VmwB9gQBfl85JxvdEh/IL22nSWciWh8lPCDEF+KZ0TjIpBDiP0pRTiAuu2XrS2UIMAf7KtpDtO7af2JavJ08mKYSBMo6SzkL2zGf7XTpbiCHApRIXAa7K9qN0OnIQuZUhQRNoXPhXOjJkH7YLpNMCBlBw7daXCQ0UAQZiEwdWJswl+3Zt/MH2vXR2cBHb/hReXmquobxjXYvtJLaXyF+AAMfm0hccRIDLkJrXGmdcKg+O02W7JrDfbtLpQGh5KUHLYA8aj1ifpTABYlDE5fiSC/ArUoG5BJczLvGHCjC0+QlC90vJl9XnOMQaKsANSR3fBjJBkFyAYAGNx8nvwiX+UAFixUvIfiB0v1Scb3zPPVYAAV4onY7g+M6WTsEgAkRg70rnmOFSeUIFiH1C9gOh+zWxAs1ccTEKyM+sbDFj1cTOEwK8WDodQSxfS6dgMAEeKp1jhsuFHkWAoQtrQ8prY2WKK0BMqTxlGGLFZ0xiHj+AAC+RTkcwymuLJ7kAD6eZQeE2jRG8cUIeQxOjCPA+6XQkpLw2sLg4pgAlMWPVxM4TArxMOh1BX9cWT3IBfkDTQWHh6mdss9kWLdliPLCd2D9penXCD2zn1JM7Qd6XSqeFR0mVg/JQ7l/15CBWp34EiNaPjhUrN2Jiuy4+/ExqKghxYkmgLy+QPZ7kAkRAH7GtyfZg5cOcly1QX25gu63FbmG7me0mthurbfdevJc7sePVLEcqb8xBDU1fAuyTvq5LCGjF2OIZRID4a32dTBBgAhR3RgmmMXLAdmJD2ZhU3kkvCrN9g+3EdkWDHzY069DMmGA4d9IHm6N2SwpaMbZ6klSAaHogoHeqzyfqyTXOlY6KM6VjILpOLNLazAae/cN2LoNUMu8us7Ffgx1CqqUg/TAbsvwQ62IzmhkTDPtJH2wXtVsnsnyb2UDf0bZdUgG+R/WA8P0q43dMMLCDCVRX21ft5oztxIaClezI+1SZMAClCToa6GLZ4kkqQARjzv/h9z3Vd90Z34jU0DT6Zib3sr1K6q9yDthO7Cggb1sTPQVFgKPxFtnjSS5AORF7DKnh+ucrHwZosBD2H70RcwSpbeaS3wLlPrGdWLAXqe185/Swj+v7X9AUe5/tbZkQgRgCvJXczlUsRi0L9RF5HCgTAsAoqi2eZAJEp1kGo9vs8pEdDMA09YEeoNErRCzksUgwiqn7sbi7+zS1kfeH0tkBxNdHyyCGAFGR0fVIhe26uBAjD4B8bHklE6APbUHDn8vTvm0xasx0LMHyweXCmfhs60MMAWLAremPaV/EOBcx8gDI5xvpFGQnwJ1JNUNx8deoJ0U7MTHoimVLUumYfEfz8Mp6shW9TMsVve3xpOY4tzDShkbHhqcDHmG73UjrA8yjjgKeRMFiEfA423NGmi849rbRfE12AgR4nP8u4duGZjZVh6RLIEeSSl+l+v0Q27FLUu0cRmp/l7s9Kgyaq1hMALDfVtPJg4N4tmObIlWh0Y3IGdyxsVxSj0l0Xecu8L8asO+U8EuyFKAJ7oQAlfg4M2Fgui7M7lRPP1n8dgHbHy2dDSwgtW3TSp7r2VaUzoTMIxXb6TIhYxAvBgA3kQkVWLXlAloiLtc8ewHiIPD0PNZW5kTXycUT32b6ieK3CzjeT6WzAZ0vJn2fNBMyAH8cULnQJPY9/qHQcaLvtqOZ4AnyMafc2shegLPI/lTxENgqlJl+B6m7kQ+4KLYygN4GT5M8zbY2qRfEornn+te6L8z49Xe0BjAijJFRPJy7LtvdpO7UQ7+kCedQj9i+QWopnl4Uj74l+rEui7L1el6X165kL8BcsYkDc5l4VfmdpC5mCCij62ls9PXMu95CUutsNR8b34fAFBReGvtF9d18g/SuNL221HZO+wb9U4gOQDwYQNuz+o2Ywf3VZxfPUH0eu4siwEBSVJYDKLwcDCRMkRoMyJEXq089yjib1JTHCdXvHEE/e2vpbADXzHUkuggwkFBh+IImD0ZFfcEE+OXSmQl4X+YO1fdF1SemnOaTWvGUK1gKaQOvr/hEOjsoAgwklQABynKZkij0A5rIeDuA7eFh9Gd960URYCC+J3oU5pB7n6IQHzyjeZ50NoA6IReP2CgCDAQn27S+weoazIUW8gRTRhh4c0HWnSLAQmGS+R/adfvHplLddQAAAABJRU5ErkJggg==>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAAA1klEQVR4XmNgGHaAEYhV0QWJBU+B+D8Ukw2uMFBoAEjzNXRBUgDIgAh0QWJBFAOm85uA2B9NDCe4yYAwgAuI7wMxHxB/g6sgAECabwOxIBBvhIr9hIoTBUAKdwLxTHQJNHCSAeIyFAAKOJABV6H0HlRpFNCKLgAC1xlQnQpiT0HiEwTo8Q/ir4SyP0JpeSDeB8RzoXwUANIQhsbPZoDkjWNQMVAACwHxX5giGBBjwAxpP6jYBzRxUACSndBAAN0ikoADA8QbvEAsgCpFPPgBxMvRBUc6AACBBjEqtbe1aAAAAABJRU5ErkJggg==>

[image34]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAZCAYAAADXPsWXAAAA8UlEQVR4XmNgGAX4wFUg/gPE/4GYE02OJLCXAWIIRQBkAFUMmY4uSAqQYoAYIoEuQQqYxYDqlTYgfoomRhAgh8chIOYD4lVIYkQBkOK5QHwJiFmhYvOA+B5cBSpgRBcAAZAhO4F4JroEFiAHxDfRBSMYIIaAEhyI3oMqjQEUgdgAXfA6A6rfQewpSHyiAEjTNTT+Sij7I5I4CKBbCAcgwTA0fjYDJPCOIYm/gdJfgFgXSZxBjAHTZD+o2Ac0cRhAV08yALmOYkPygXg7uiCp4C0Qm6ALEgtA2QAEyPZKEQMkRpYDcSGaHEnAkAFHfqEKAACDWzfasyyK6gAAAABJRU5ErkJggg==>

[image35]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAYCAYAAAAs7gcTAAAAmElEQVR4XmNgGJSAEYhV0QWxgXdA/B+KiQKXGUhQDFJ4EV0QFwAp9kcXxAaCGBBOAGlYBcTRCGlUALIepPgPEGtCxUD8ZXAVSABbSPzFIgYGIMEwLGIH0cQY/KASyAAUQSAxczRxhtNQCWQwG4sYGIAEr2IRuwVlv0SXCEYWgIp5ATErEG+BCYpBJdDBIgaI+Dl0iVFAMgAAuAwnpyNJW1MAAAAASUVORK5CYII=>

[image36]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAYCAYAAADkgu3FAAABQUlEQVR4Xu2ULUsFQRSGX5OCikEwC2IziFhMgorN7i8w+BM0KwajGEz+BLNYDBq0GPzAZrKJioLfH+/hzMDse2dvmHvLhfvAww7vmT07s7Ms0KXT2KbP9C/4Rh/oV5KNxsntIDZVjuD5mBZKsWYnGpI5eO1KCyUsw5staIHswWv7khdxjfxrM+peaRG5ZpP0m95J3hL2EPvSzugF/QhZbzqpCePJeCAZV4jnY4eechPyOobhC9qgI3SFrtLPdFLKLfINt+C5NVFm4a9VOaebGkZy52O8wvMeyW0nufnGGu3XMGI3nWqI+gXYX8TOMseEBpF1eLMlLaDxQXFs15kkb8oOfaGP8K/tif5UZvjqrOk9/P83GHLd5VTIfsN1vloux5r1aQjPhzRshUN6KdkiGnfaFnbhjQ/oO52mx5UZXTqCf1KmVZXkkkUVAAAAAElFTkSuQmCC>

[image37]: <data:image/png;base64,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>

[image38]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAZCAYAAADjRwSLAAAAmUlEQVR4XmNgGBRACF0AGTAC8X8gPgqlQRgD9DJAFIKABBDvRpKDg0Qg3o8uiA2ArFBCF0QH7xhwuAUGYhgQDr6DJgcGH4G4Ecr+wYDFtBtA/BqJn8YAUSSMJAYW6EDiW0PFQMEABjpQAWQggy42CV0ACMrQxUrRBYDgMRAvRxMDK+KAskGORdcEBkxA/IIBIvkWTW4UMDAAAIETI1FLve9bAAAAAElFTkSuQmCC>

[image39]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAAAmElEQVR4XmNgGDlgMxD/JwHDAYgThiwAFUNRBAQayGJCDBAbkQETA0TBBTRxEHgEY2wFYkYkCRAoYIBo9EcTZwPiPhgnH0kCBt4zYDoTBASAWBxdEBlg8x9BwMwA0XQGXYIQKGeAaPRGlyAEPjOQ4UwQIMt/oOAmy3+zGSAaE9DEsYIgIP7GAIm7t1AM8ucvBjKcPAoGBAAAiastbKanIo0AAAAASUVORK5CYII=>

[image40]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAYCAYAAAA20uedAAAAcklEQVR4XmNgGOTgGxCfQheEgf9AXIAuCAL6DBBJJmRBGyD2AuLdUElfKB8MioC4BCrxFsoHYRQAksxFFwQBXQaIJCO6BAisYYBIYgUgiXfogjAAkgQ5CgaOILHBkipQ9k9kCRDoYYAo+AHELGhywwEAAMS4F/hUVNxNAAAAAElFTkSuQmCC>

[image41]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAZCAYAAAAFbs/PAAAAiklEQVR4XmNgGAXDAswG4v9AfABK16HIooFfQHwBTQykyRHK/o0scYMBIokOQGIgg0BgN7rEc2QBKPjHAJEzB+JomKADVNAdJoAEHjFA5FBsX40ugASuMUDkJJEFG6CC2MBFBhxyIEFVNLF7QLwWKgcCfUhyDEJA/JcB4d4ZSHL3oWLxSGKjgLoAACgOJkiAxK1GAAAAAElFTkSuQmCC>

[image42]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHEAAAAYCAYAAADNhRJCAAACUElEQVR4Xu2Yu2sUURTGjw+wEbGxEUvBQrJp7PQPEF+FtY2tISCSPmIlmtpCURTxQQh2omIIWySNSREIKIjYKCaIplJR8XW+uTPOmTN3ZmfurjOrnh98MPf7NrmXe3bvnBkiwzAMw/gvWWF9Zl1i7VSZ8RfwlbWFtYf1k/UtGzs+sZ5o0xgaULie4EOntWkMjPvaqMlr1k1tSkbJFXGjDoyB0W8Rd5OrEY7TDAdYh1iPyX3gaDxukzHWXdYRHTRMhzXNOq4D5qA2KtBvEQFqlDtWz7Am4uB9PIbaYIr1g7UrHj9nvUljWhTXf5o1SjcMWhDZVtZlMa5KP0V8SK4zPUxuPbPZ2IFgXJsFXCF3Nvt0g3WddY11Nf4sJu4F/jb3DSPn7WVtprCNC+Eea1mM91F2bS/FdR1Ci9hlPRVj769xJDY36KAhdpCb/5QOyPkzrAc68IDNrqoyPmqDmWSdja8fCd+HnisRfs3ag8r6kOQ+KMGjhvaiTcqZDdKl4vnhP6PscVbEsRoKAZuHe2Qv9FyJljwehGe/IlYpvzcvPF5krGuzhHOsCzWEZqkM7/EQU5Y1DdbxQZs1CDlOMecdj3dLeZE5Icbz4roJ8JKhqFDw32mzJbAWdPOhhBbxosfbpLzIxNkLvsigIfZTvojbyXWqr0R2Po1bQa+xLiFFRJ8gX6/hf9wW49+gtccC8WIVXWAbJK1zopMiwxcL3jbhtcF3bdQkpIjgBKX7gtuTEUiHqjU1ZYQW0RgQc1TtedcYYvq9HxpDwFttGIZhGP8UvwCSo5pMsRFGgwAAAABJRU5ErkJggg==>

[image43]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAYCAYAAABtGnqsAAABwklEQVR4Xu2YPyhHURTHv0iZLBZiMFiUUGzYTEhSYpQsSiliMTLIoMhIRDEpymyySYrdYlH+JLGIOOd37uP+jvvze2949yfup769+77nnO75ve7vvj9AIBD4YwyT3klHpN7sUCAfA6R+M76FXMj/BP/euHozNVmskjq0WSDOkaPJlCiCXJhqyys23oXlMTukQ+VlqMPvWXXcx742U2SJ1KK8CUgffcrvJo0o7xMuONOmZ6LV0KwDKeJaOPdw+3Okcm1GHECKOnXAA/WkLshq4B74JsbnPuBVpYn2O40rF+2Q5CZzdBWmzRhpivQKmX/SqBCUQHo41QEXtci+YNEqzMcgaTuHtkibpA3SOmmNtJypyg/PvadNz0xD+ujRARecuGCdtxmv0vJ8Ee1/jTqQg9YESsIj4i0iNOB7Yo3D88U4ks3N+2RcJSH2NraC74kzDs8F32gWE2heyn7kBvHmTpNSSA8nOuAi+q/bXJF2lecL7sV+SH2wxr6YRYL9j+HkMjOuMOeFguceNeNLfPXlkxdIH/wmEgtOvIYU3amYb4bwtf9UqVia8KvjE+Thmb8D8PEZ8kh1bOUFAoFAIBAI/AU+ACqce3FR6kdgAAAAAElFTkSuQmCC>

[image44]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAYCAYAAABurXSEAAABpUlEQVR4Xu2VPShGYRTHjyxE+UgpJsmCiAWjQSGTiZ3RYjBhUZKvUBSDxWJQGNmMFIOyGw2+DcrCOZ7z3Hvuufc+3d73GtTzq3/3nP+57/P8e+8XgMfj8Xj+E5uoSdEvoWZFnxd7EN3H0qMNF/WoW66nUF+ob+6vUatc5wGtXQpm/X7hT7CXGXlyJfedqF6ux8S8GPbBBCZo3WExe2QvM92inoHoj8tEbRlBLWszA3N8XIF4QOqPRV+BehW9k3eIL2ipRU2jLqGw0BZa/0H09nbp4n4bzP2dliMGnXigTcUFFB96VPT66hIlCV5ANZhhM4T3c6uY34na4go9hGrTpoAeeh3mLcFzht4FMyxH3XDdxDN6GA+5llBoui81dqPUzRiad3Ddzv1JOP7FGVpuNADmH7f9vDhPQqHXtMmcou61qbCvN9IWH+XVJZyhC4FCr2tTcKUNQYPqzyA53J+E3tCmIG2zGjCzHe5tsMHgjJBcQ9Mr8QnMx+BDzYhzVJ02mUbUJ9dVYEKNh+MA+mo+g9njBbUQHedPizYUfagj1KIeeDw58AP7tWNIYJrvsQAAAABJRU5ErkJggg==>

[image45]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAAYCAYAAABurXSEAAAB0ElEQVR4Xu2VPSiFYRTHj49CyUeUopQkhYgFizIoZDKxEQbJasIoxYJSDEpSBoURm1EYlCyS0UDCQFKcv+c895573C+5BvX+6t97zv+c5+Pe93nflyggICAg4D+xwBpR+SxrUuWpYpUi1/E0WyMeJaxzicdZb6wPyU9Z8xKnAsydQW7+duUPi5c0ujlX8gZWi8R9qv4b1shtGGDeblW7Ey9pmlQ8QZGDs1UMcGRQv2flmVoipuQ6R983iHxH4jLWq3hDoY44PNH3CT1YNFPiaordlwiMu1W5Py6Nki+pGvxRlUcFTRvWFK5Z7ypHb4/KkwXjelWu7265isG+yb8oELOSwue5RtUvVGxBb5Hxuli1xtPgobebeIzieZ5ZJ9ZcITcgh3UmcYXU8DBuSWzZJNevSSM3PtYGPKjXS1wn+W64HCKLYsylF+og94/7fFr1abDQkTWFPdaNNQ3+9QYtylXfXQ987O/X5LPWVd6mYs+xNRSlJo96ZpkHFV+p+MfgV+OMD5B7FeFfStcNQrRNgEJytWXJ/V3uDHU4LlmDojHWYWT5Z/jXoZblgFVsTQHv3xeJcccwvj9c/gLfDLsGvtJ/SpU1DK2sbdaMLQQEpIBPLahu+pK2NWAAAAAASUVORK5CYII=>

[image46]: <data:image/png;base64,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>

[image47]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAYCAYAAADpnJ2CAAABNElEQVR4Xu2UsUpDQRBFr5VY2Ap2EsHKwtJAqpA2vZXYKPgN+QELSyurWPkFKQI2EbQQQRsVC8FCLISgoiKioneYXRwnm2q3Cjlw4O2dfbPLvuUBY0aNbfpMf4LvtE8/TTYXJ5ckNvccQPN5X8hFmh75kNShtQtfyGEF2rThC2QXWmu7PItLpI9TGHbUWaSaLtEveuvyIshicjNP6Dn9CNmknVSK+P3kcliuQl6ca6Qbb0HzGV/IJfX9hFdoPuELuUjTYx9i+EbO6BNdoD36RqfoPt2jN39TB2lBmzZ9AYMLyvO6ea6F59UwjqQ2iR36Qh+ht1N2/P1vBrAIffke+n+dNjXb9JCumXFywRw2oP/XiF1ATkouYVHuaNWM7YIPdJl2TZaNXaBCO2a8SU/prMnGjAC/iedUbiUnRA8AAAAASUVORK5CYII=>

[image48]: <data:image/png;base64,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>

[image49]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAYCAYAAACfpi8JAAABWUlEQVR4Xu2UsStFcRTHD4ooC5vBYGI2KGW3GhiM7NiUUkpKDAaZxaAQi8XgH1BWqzIoi5AFKb6ncy/nfu+5v+6kXt1PfXrvfr/vnHfv690r0tCifMBuDv+bFfgNH7hI8AjfxebUoWItU65TP4t1jB/opC5FO7wRm3umLke7WizBdbgqNnRXrJMswjH5u4iILw6q8AvyhR0uS/GUvU6LzZ24ThmGW5SFzMNtd7wptvDWZSmii/AcwV7KQnhQiRZGtMELd3woNjfrsjp7ZAbucQh2xRZcc0EswFHK+CJq3ylV8MKI/P/h0Vta5/rhCNwo1mUm4QGHjn2xhVdcOKITHRDL7+Ep7CnWZaIlTOpX0efHJYcZ+VzV7C/j8IzDgHOxZdFnl+EEhxlzYnP61E3iz7iunr4s02dHFdqvcegZlPKX1HFHh8ErfBH7o+r7tyxnjmEXhw0NDS3PD38+cdT8Dfx0AAAAAElFTkSuQmCC>

[image50]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAYCAYAAACbU/80AAABTElEQVR4Xu2Uvy5FQRDGvxCExhsQTyFR6CQSlYZK5QUUohAqjeQWJKKRiNDzBF6AkmhF4wEQiT/xZ8bsuZn7nbF3NXKL80u+ZHe+2T2zs+ccoKHHeRUNc/C/WBd9ie7ZyKD5peqKTx4kL0c/bM01G4kWCgpYEW2JNmHJt512llXYmnk2EkOiKw4yvsKqC3qyEh5QP+G4aCKN+0R7zquxDGtTxTZswxsXyxHd8aUbawGjbl6DFyvRphHV/d+JJkUzosMUK2JBtM9BWMt0kws2iDVY3gmscwdpXvwO5Sot6cIT6jmLoiU3n3bjDmZFxxx0HME2P2fDERWpXfG80bwNL4yIHlAxgO7XpNcSdmBKdMrBgDPYQ6LcDZg3x0ZiBL8X3z7ZX8S8II7rl6E/NfV2yfthDPXNS7Sji4VH0YfoM8hRqfcuek75DQ0NvcU34jZ3g7u/fpAAAAAASUVORK5CYII=>

[image51]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAABOUlEQVR4Xu2TPy8FQRTFjxCNQvJKH0BIJKKTvIhEo6ATnYgGeQofQeFT+AB60es0CgWF0FD4l4jCn0YlnLt3Zt+da8ja7iX7S0527rlz98wms0BDL9OiHqkv6oYaTttZ3qkl5+1RJ9QHNe56BYPQoEgfNHTKeJ5N6B4btkINmXrHrEtevUEmqE9vGp7xM0y+yDPmDRnqOG8y+Dni4XzYOjVg6i2zLnmBDh4ZT144Y+rIKrUW1j5MOKQOqGtqzvUK+qGDURK0mOzoIpcikgurxAjSwIu0XfAEvTyRWmHz0KsqzKIbeF7uABaobVMLtcJyF+EWqR8PY/l32DLyYYL402F97HQa+pehroT8uH+F/cYoanyZIEO7zpP6zHmWNnRuwzeq8AYdvgrP/bSdIP/lA3VH3Ye6oaGH+Aaij1DvEychWQAAAABJRU5ErkJggg==>

[image52]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAABQElEQVR4Xu2Uu0pDQRCGRxRBhCiWPoGCIMHGRgQbG1ut7ETQvIMWtr6AhaW9WGsriJWCt0YLC1tvoDai/5+9ZHY8E7AMnA9+svPN7mwOnESkppcZQ56QH+QBGSnbmS3kDflA1kyP7CFnyCcyaXptBiVclOiTcGlTOXKDHKv6CjlV9SoyrOpttc68WAGmkG9VNyR8AQvdaFzziSwTVvDApnHT0ScuTJ2g24/rdWRA9VpqnXmWcOhEOT7tnKrZ9y7T/gg5RO6RBeUz/dI5xPCipWLH36EJz3dlXMoLr8u2O9TzLosSXlUyL50Bl3mHP9TzLlWbH6X03lDPV7Is/mb62bh+j7WF7tZKD/5wq4YQ7VdMnaCbsbIbPLBjHGv+tjTct6Hq3ej+zauEg3fx86BstxmS0DuX8PJ8Sfhrq6npMX4BHbRcu8/0+OEAAAAASUVORK5CYII=>

[image53]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAYCAYAAAAcYhYyAAAA6klEQVR4XmNgGAXEAmV0ASgQAeJ0IOZBl0AGb4D4ARBnAfF3II5CkqsAYn0o2wmIg5Hk4OA/EDej8UEYBnYgsUHgBhqfYSkDqgYQ+ATEx5D4G5HYIHAJjQ824C26IBroZICECQgoAXEKkhwDPwPEkF1APBHK/gPEiciKoEATiDuAWA5dwpEBovEjA6okSCwfiY8XgGwEafiHJn4VKk4U8GaAKH6GJr4PKk4UkGeAKF6MJr4JKm6KJo4TgBSvRBPbChVXQxPHCUCK76CJXYCKEw10GDA1gPiNaGIEQS4DRONdKN2OKj0KhiYAACCXNRnS/vubAAAAAElFTkSuQmCC>

[image54]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAXCAYAAACMLIalAAABpklEQVR4Xu2VzysFURTHD8mGJTY2r9hYKHtKycJSwl7ZIKLs/MgfYKNYykYsKFaK2IhiQ8RGNmIjpYSNiPPtnJk5c95M5i2UxXzq29zv99x75943c+cR5eT8PZOsIR8a5ljfrC/WdLwU0sg6Jem372qgmmT8Luvc1ULWWR8kk0DD8XLIAavD+CnWi/GgnWSOgBbnwaXzO84XkbaoctajD0n61zvvf2ls+MT4LtMGSfPGSFtUNxXvGCAraLtOPa6WPc0Djk07yReRtqgqih5vg2ZN6gNmnQ9YoXhey3plLbLuTJ5K2qLAFkULO2O9xcu0rTXPEiXnmcHgER8arihaGNRsaoeaeRZIcvvulQQGj/pQeWf1afuGooXhiIM19R48JuQVvpAVDB7zIbPKOnJZG0n/a/Vp79QyJeeZweBxH5LkwQtumaHohq3a/u30lQwGT/iQJO/1ITPIujUe/XqMBzgQzy7LTA3JpPO+wPRT8m6RVRqPv45P48tI+hRMlokN1hPrgXWvV3xl8SW2DJDcADvHjdHGRjwXJIdik6RPZ7yck5PzP/kBWQRz9AqWWSEAAAAASUVORK5CYII=>

[image55]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAXCAYAAACMLIalAAABWklEQVR4Xu2VPUsDQRCGB7SwsNRSCwV77e1tRIiFgp2d3xECKUVsLNRKRH+Bhb1gLTY2gv4BRUHFMiB+ou+4G7N5b5YkeoLFPvBwtzNzey/HJSeSSPw9JTjDRc8HXIPTcApOwglvTzAXUhB3XUgnfIdH8Ix63+zDF3EXq7P17S96pda31L5FtR9yTutDWmeIhZqDW3AQDsB+2AfLcC+YC7kTO9QIre9pnSEWSh810w4fuegZhctihzppsM4QC2XxxoWAJ3+0QnXDCtyGV9QzaTbUDlzloucStvlzK1TL6Ab6/jQidqNhuBKscwu1wEViQ+I3eqV1bqEWuUjozCkXwQXsoFpuoYpcJHRmnYvg2LAaSs/na6OtoRvoTznGmLiZJW5E+PWT6hK3gb4zMXbFzeinphl+HOoAPsAbeO2P+i+rnx5mXNxNhrhBPMNbcfuput9m3UQikfhnfAJFNGY/GVkBigAAAABJRU5ErkJggg==>

[image56]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAAYCAYAAABJA/VsAAABi0lEQVR4Xu2XPS8EYRDHhyhEIaHQ0YhS6xOIKIQO8RH4Bko6pWjkhKDSCBqR6CRUOq+RkBDRebtEQoEZM3c3O7ubvWeLew7PL/nndn7z3OWZ27vdO4BA4N/QgOmx8i9zj/mS1BNNmA8rq2AJeJZbTJfpRTiB+hn6AionwXVPn5gBVdPzB1UdgZpnVnrmFdyGnoX4+qEEV4Ya41Z6xnXotBNHvtPKCWloZjAjxtWaPEPvWwns5628lAbRgrnBtGLeyiv8kGfoHSuB/W6SvMK0YbbFvYvPYj0la5hVzApmGfiKWpDnVIvL0I3AazdtAyrzxeQeZtE2POMyNEFrt6wE9gda0MWL5Kk8Jn0nfJFnaDp5FvKRT9m5yBJ0vKDqLOYc40KeodOu3mNW6IVUb8jxi/I+yBp62tQ0h13fl+B+xKipp4B/ix8q7wO6e8Q2LDwB9yaVaxfXrFwRc6xq6ID4iw6Leza+ltBGHzB3Evpv8IjpVmt6MdeqLtEPvH+6C9EbcxRtBwKBQCDwK/gGbg1/w7aas8sAAAAASUVORK5CYII=>

[image57]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAYCAYAAAAcYhYyAAAA2UlEQVR4XmNgGAWEABMQC6ELIgERIE4HYh50CRj4DcRTgLgciP8D8X1UaYYKINaHsp2AOBhJDgx+AvFmJL4kA8SgPUhiO5DYIHADjQ/WAML4xDYisUHgEhqfgQuIrZD4igwQAy4giXUyQMIEBJSAOAVJDit4yYDpMhDQBOIOIJZDl0AGrxggms+gS5ADbjNADGNBlyAFSDNADNmCLkEqQI8dguAvEM9GE4MZYoMmjhWAUh42W2FizGjiOAFIMTsSXw8qtg1JjCAAZbp/UPyGAWLAVBQVo2CIAgARNi5Td6wUfAAAAABJRU5ErkJggg==>

[image58]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAAAXCAYAAACChfjKAAADw0lEQVR4Xu2YWahOURTHl7mMkTK+eTBEIg88oEQU8iBJKaUoQxRJypSUIaEMyYsHRCQkZEjJizI/KLOLjMlY5mn9v72Xu/a663xT3TKcX/27Z/3X3ufsb5999lnnEuXk5Pw9DGM1tOYfQGNWPxVPUsf/BD9Z+635B3CRwtgEHM9ScUI71hMKje6x2qTpBNzRL9aMbGOdZ31k9TQ5YSrrKesba7XJabCaL1EY0yMK1xUwXvhNlAeusAazmrK6shaz3iQtArsp9Mc4V5pcKU5T6PueNcXkAHIH4vG4GLtgkJh0oQGFxvpxATeiL7JMZrVQ8VJ1LGCF6mvtYr1SsdCfwjU6xHh8jIUNrB8qBrgxenyQt0Dgt4/HfWP8vTZdlM+sRvG4FYW+D2vTBeDJFoiFUFObSvFWRG/KHsw78iceK93Sw8Top1eueKNULDd+gPLszcbYJqhYuMnawlrD6mxyYCHrKqXvhgUUzr1eeR5YSGi3RHl2XGNZX1WMnDeOAkjOMJ6sBI+siZ9G6aTOVMdgI/n94N1RcU30NJgova3YvHDWGgYsDvTdbHw7gR59KLQZozzb7wKli6joOV9TaIC9S8BTgL3SI2viwWHWQdZdClWHBo+9188OXse9WB1VDjRnnTCeUGri0Rf7r17xzajuGMoFfbDX61gYwVqk4jpgz5ILQ5h0fVctxSa+GFk/zvo4fsB6QeElOjt6+v2RxWUKL+2jFPrfT9MumBycP7PycEDx8Zb1wSYqBfuQnvzraTqhPie+k4kFTKD1PD6ZGH28d5gGbbwXfBbY47dTqIi2mlxFjKRwEjCUan/4td8tUupz4rGqvXbyYutu/FLspdAv62m5zXppzQrwxlo2XkeUSJ4Pqp14bAFePzt4HKNu18yLPiqQSlhOod9E4wPU8sWe7HI4QuH8e2yiFCjJvMkA8Adak6qf+FPk94Ona3LEz1UMpOSbbnyNvYFgXfSGG38O66TxbF8LylD8dg0+0NBPl5BlgY+krAtm+dVOPKoTrx+8+SqWL2iNlKKo8bNAHh8sGikfNUNYO40H7OpfZmK5saiMBHwAwsOWVjHouMJ4iHGHPfAmtz+mXLCy9SBHU91zyT6PikZAfEbFHpsobEmCfMnuUF6X6Hlapdodit4+5WH7W6tiIH2rBqURTiD/FsCdtKBexf9YMADoMYVqoJtuVAao52+xzlG4Vss0XQA1MHK4Bv4eT9OZHKPQXp7KuWm68DK1Ey4apNq1pXDt1soDKDjQFl/I+PssTefk5OTk5OTk/E/8AjNINkxZi3JRAAAAAElFTkSuQmCC>

[image59]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAAXCAYAAAC74kmRAAACk0lEQVR4Xu2XTYhOURjHHx/FJBJmMyzGRz5KkllIiYUlEflYSBYkG7KUZmqSpGRjPfthISVZsFJjg4REPpJC+Ur5JonnP+ect+f+5z7n3tdiYt73V//mnN85586957z3PecVadNmNJjAopU4pxnP8l9kiuay5rfmhmZcsXm4/kVzXvOG2nLgeh6vWRgmau5KGI9+84rNDfo0HzVfNXuoDRzQPNa802yktgazJfyjjlifGet25d6bMnhF9TIWaXrJ3ZZw7RSPn1JchA+avaYO7muumPo9zTVTn69ZYuprNVNNvQFW9iy5m5rvpn7ClAH3L+MZC8MF8ScAbfbGE7b/NKon4KbHMt8z2M8CYNB2ckeiT7w1ZYAVqeIHC0NuAuDPkMOnwfZPnyQGbiCWF2u6TNtSzQxTH2aNhEGrye+OPg3AO4lPxCnN59Qpww7NZpaG3ASk76Inxt2S8L4n0F42nv0xzVXNdc1B4xsckjBgBflt0a8kXxe8wzlyEwDSgyAPNf2F1pEPmvC8y1EJA5aRx+rB7yRfF7t6ZVRNwGQpTgJ/CXsP6nmXfRIGLCe/Nfp15OtwXLOAJZGbgLkS2vDed8cygu0u4T2o513Sd8Aq8ruixxbZLHVuIDcB8LPI4T2G74x170E97zJJwoCqXaAuOEvgsFSFNwF4wDIP4A/H8qdYZ+AesKwCg06TuxR9s1yUMKlVeBMAcn5OLGPByvrB9bCsomy1Ud9Crg58HY8hCX3LJgvvOrZCC46xWHULxtuDzcno/opBza/4FxfB9tgsC2XkdsV8k3CMfqF5rnkp4ZzO5/hHEu4DWyD+Yh9n8LqltjsSzin8G2ZUecqi1cgdfcc86zWbWLYSdX4fjGk2sGjzH/AH3Hi4Bs5t5eoAAAAASUVORK5CYII=>

[image60]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAXCAYAAACmnHcKAAACfElEQVR4Xu2WS6hOURTHl3cRumJAcQ3kUbeQieSViQkTZYIhiQG6ipRuwgilKJQykAmKmEhhwEQGQl4TkjwzuEREXvtvrbW//17fd1yuDOj8avWd/3+ts8/eZ5+zzidSU/M3WJCibzT/Vb6lOBlNMCLFM9GChymGl+nMCdGajyk2hxw4lOJqig8ppoScs190jC8pdoccg4mi7m6KwSGH+SI3IPgyUHQhTh/RwunkAXjDgv5EekWKIaS76NjBIseTxhgIBhOEN850P9Ojc4XI3hRfSWdeRyPRIXrnnLmiA14kr9u8SaaxI5HJdIybhvq35J02bzV5V1I8IQ32SLlozG0p6QyK1gRvqvlOf9O7yHtvnu/WKtE6Zy0dO6i/RvqceYvJgz5AGswy34m7mfE7fIE87NYc0q3AOXHQM6J3+4Fot+mJOIY/UlvJA+3mLxF9f86X6QY+gAcWsqioKMHdvy36zOL96i1nRa/HzWaaeZ3kgVHmt2o6TYyRckF3ynRmWYqDKV6KTqY3zBTtaPdSXBd9lxzsJq6/jjzQZv7h4DexULTLgHnSWNDNXNGaF6J1f7I7l0THGGl6oukNuUJBHv6O4DeBoshjae0zG0VrnsfEbzBDGjcP+GdhS65Qxpq/PPgFaG9Vk4aPRwIcTfGZcmC2lBPpCXQ31A4NfhwDx1XdjL81TeDDWDWZeAHEfPJWmveUvJ/hY2wjbwL5DhrLLdJgk1TPswBF24MHfYM02u1l0uCd6LmDgl/FetH3jEFXxBjt5PmOM9D7glfJG9ET7tvvsTL9g1OiuUf2i6bxqwtxdoqe+8p+sQt4HyK+E8dF/zIdKdM1NTU1/yvfAYmEr/p5+63wAAAAAElFTkSuQmCC>

[image61]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAXCAYAAACmnHcKAAACUUlEQVR4Xu2WTYhNYRjHH5+FJDILC+aSMKHULMhHyt5G+Qo7UtSMLDClacQKpcg0pZSlLHxsZGPBgoQiUcqOIkXTTE1Nvp6/53lP//PMPefcqyzo/OrfPf//87zvOec997z3itTU/A22qCbH8F/lp+pGDF+oHqsOq/apdqt2qXa6mGOqcbGJNocaGBKba0zVFWqJS2Ljv6vOhRqDC0Xfa9XMUJvntWkh/x0W6Sv1jaqekv+iOkt+r2oW+X46TuAmG+TTeRhcILJF7qe4X5B1iFxQ/SCfgcZNqpWqpaolLj7J5eBBR8jwRCIr6Hi6WP8IZTc9O0jZQ9V78uC85M+Fp7qdfMazGCiPVKvIN1tBgOyEHx9QTaXaITpOoP8J+buebaUMfpA8WO95otm1NAUD44tVdjMfyd8WW+13YrtNFXHe9JU6SRno9Hyb2PtzL18upuii28lb4Y7Y2DmUrfHsKGUgfaWPh7yUa67IKZl40Ts8i3kV68R2tDeq52LvUgJPE/P1UAbmen4l5KVgQCOGDnazB+Q/ifVjq/5T7ovNMd/9MvdHsg4DdeSnQ17IfqleZWy3w2IrC9DPN9gu3ZJ/upP8uC/rMBZ6vifkhbyV6pthZoj1L4+FArC7oX92yPlmki/azfi3ppQ4KdMpVltL2S3PWiXNP0AZftfiefFj+JI8wD+Pds41YVJmg1httXusLvzirKOaXslv4+CV2DxYrMRGzxj4iyErBQO+xZBIL/wH/2zkqq1xRmzsZ//EU8D7EElP4rrYBnM1X66pqan5X/kFKm+m6KXc5LwAAAAASUVORK5CYII=>
## **6.4 Practical Programming Task: Coordinate Transformations**

**Problem Description:** You are analyzing sonar data from a survey conducted off the coast of Italy (15.0°E, 50.0°N to 15.1°E, 50.1°N). Calculate the Euclidean distance in meters using UTM Zone 33N projection and compare it to the true geodesic distance on the WGS84 ellipsoid.



```{code-cell} ipython3

import math

from pyproj import Transformer, Geod



def calculate_utm_distance(lon1, lat1, lon2, lat2):

    transformer = Transformer.from_crs("epsg:4326", "epsg:32633", always_xy=True)

    e1, n1 = transformer.transform(lon1, lat1)

    e2, n2 = transformer.transform(lon2, lat2)

    return math.sqrt((e2 - e1)**2 + (n2 - n1)**2)



def calculate_geodesic_distance(lon1, lat1, lon2, lat2):

    geod = Geod(ellps="WGS84")

    _, _, distance = geod.inv(lon1, lat1, lon2, lat2)

    return distance



lon1, lat1 = 15.0, 50.0

lon2, lat2 = 15.1, 50.1



print(f"UTM Euclidean Distance: {calculate_utm_distance(lon1, lat1, lon2, lat2):.2f} meters")

print(f"True Geodesic Distance: {calculate_geodesic_distance(lon1, lat1, lon2, lat2):.2f} meters")

```



## **6.5 Real-World Case Study: The Cost of Incorrect Projections**

**Narrative:** In 2018, a commercial dredging operation in the North Sea relied on a hydrographic dataset provided in the Gauss-Krüger projection. However, the vessel’s onboard navigation systems were interpreting the coordinates as standard UTM Zone 32N. While UTM and GK are both transverse cylindrical projections, their scale factors at the central meridian differ (UTM uses 0.9996, while GK uses 1.0). Over a 20 km stretch of the dredging channel, this discrepancy introduced a systematic error of approximately 8 meters at the edges, leading to unauthorized dredging in a protected marine reserve.



**Discussion Questions:**

1. How could a simple scale factor verification have prevented this incident?

2. What procedures should hydrographic teams implement when transferring data between different cartographic systems?



## **6.6 Theoretical Quiz**

1. Which property must a map projection preserve to be useful for standard marine navigation?

   a) Area

   b) Shape (Conformality)

   c) True distance from all points

   d) Perimeter

2. In the UTM system, what is the assigned scale factor at the central meridian?

   a) 1.0000

   b) 0.9996

   c) 1.0004

   d) 0.9999



*Answers: 1: b, 2: b*


## **7\. Glossary of Acronyms and Terms**

*   **WGS84 (World Geodetic System 1984):** The standard U.S. Department of Defense Earth-centered, Earth-fixed reference coordinate system and datum. Reference: [Wikipedia: WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84)
*   **GRS80 (Geodetic Reference System 1980):** A global reference ellipsoid representing the Earth's size and shape. Reference: [Wikipedia: GRS 80](https://en.wikipedia.org/wiki/Geodetic_Reference_System_1980)
*   **UTM (Universal Transverse Mercator):** A widely used global map projection system that divides the Earth into 60 zones. Reference: [Wikipedia: UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
*   **GK (Gauss-Krüger):** A conformal mapping projection related to the Transverse Mercator. Reference: [Wikipedia: Gauss-Krüger](https://en.wikipedia.org/wiki/Transverse_Mercator_projection#Gauss-Kr%C3%BCger)
*   **UPS (Universal Polar Stereographic):** A projection system used in polar regions complementing UTM. Reference: [Wikipedia: UPS](https://en.wikipedia.org/wiki/Universal_Polar_Stereographic_coordinate_system)

## **8\. Licensing**

The text and generated data in this chapter are licensed under the Creative Commons Zero (CC-0) Public Domain Dedication. All Python code snippets and scripts provided herein are licensed under the Apache-2.0 License.
