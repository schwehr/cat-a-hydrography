# F1.4 Levelling

## Problem-Based Scenario: The New Port Expansion

**The Challenge:** You are the lead hydrographic surveyor for a new port expansion project. The engineering team has installed a new tide gauge on the pier, but the water level readings it provides are currently arbitrary. For the sounding data to be valid for nautical charting (and for safe under-keel clearance calculations), you must definitively tie the zero-mark of this new gauge to the national vertical datum using three historical benchmarks located 2 kilometers inland. 

How do you accurately measure the height differences across this terrain, what instruments do you use, and how do you prove your measurements are free of systematic errors? 

This chapter will guide you through the theoretical principles and practical execution of levelling, from selecting the right optical or electronic instrument to the rigorous mathematical reduction of your observations.

## F1.4a Levelling instruments

### (i) Levelling instruments

The fundamental principle of differential levelling—historically termed [spirit levelling](https://en.wikipedia.org/wiki/Spirit_level)—involves using a precision instrument to establish a strictly horizontal line of sight. By observing the intersection of this line of sight with precisely graduated vertical staffs placed at an unknown point and a reference point, the elevation difference between the two points can be determined.

**Optical and Automatic Levels**
Historically, surveyors relied on spirit levels with sensitive tubular bubble vials that required manual centering before every observation. Today, the standard is the **automatic level**. These employ a traditional optical telescope, an objective lens, and a crosshair reticle, but integrate a sophisticated internal pendulum mechanism known as a compensator. The surveyor roughly levels the instrument using a circular bubble vial (to within 10-15 arc-minutes), and the compensator automatically corrects the residual tilt. These pendulums use magnetic or air damping to arrest movement caused by wind or vibration.

Despite mechanical reliability, optical levels are subject to human error (e.g., observer bias, transcription errors, [parallax](https://en.wikipedia.org/wiki/Parallax)). Under optimal conditions, their accuracy is typically around 1.5 millimeters per kilometer of double-run levelling.

**Electronic Digital Levels**
The **electronic digital level** represents a paradigm shift, substituting human visual interpolation with advanced opto-electronic image processing. It uses a high-resolution [Charge-Coupled Device (CCD)](https://en.wikipedia.org/wiki/Charge-coupled_device) sensor array. When focused on a specialized staff inscribed with a mathematically generated bar-code pattern, the digital level captures an image and performs a mathematical cross-correlation with a reference code in its memory to determine the height reading.

*Advantages include:*
- **Elimination of Observer Bias:** Automated reading removes human interpolation and transcription errors.
- **High Precision:** Accuracies up to 0.5 millimeters per kilometer of double-run levelling can be achieved when used with single-piece [Invar](https://en.wikipedia.org/wiki/Invar) staffs (which have a low coefficient of thermal expansion).
- **Data Integration:** Measurements are stored internally and can be directly downloaded into adjustment software.

### (ii) Total stations

While differential levelling provides the highest precision, it is constrained to horizontal lines of sight, requiring numerous setups over undulating coastal terrain. [Trigonometric levelling](https://en.wikipedia.org/wiki/Levelling#Trigonometric_levelling) using highly precise **[Total Station Instruments (TSI)](https://en.wikipedia.org/wiki/Total_station)** offers a compelling alternative.

Trigonometric levelling determines the elevation difference by measuring the slope distance (SD) using an Electronic Distance Measurement (EDM) unit and the zenith angle (ZA) using absolute rotary optical encoders.

To achieve accuracies comparable to differential levelling, it is mandatory to observe zenith angles and slope distances in both direct (Face 1) and reverse (Face 2) instrument orientations. Averaging these observations mathematically eliminates vertical index and mechanical [collimation errors](https://en.wikipedia.org/wiki/Collimator) within the instrument's trunnion axis and optical alignment.

### (iii) Effects of curvature and refraction

As the line of sight extends outward, the level surface of the Earth drops away from the horizontal plane of the instrument. This is the **Earth curvature** effect. Additionally, the optical line of sight bends downward toward the Earth's surface due to **[atmospheric refraction](https://en.wikipedia.org/wiki/Atmospheric_refraction)**. 

Because curvature increases the staff reading and refraction slightly decreases it, the net combined correction is subtractive. The primary procedural defense against these errors is **balancing the sight lengths** (making the horizontal distance of the backsight equal to the foresight).

**Python Snippet for Corrections:**

```python
def calculate_curvature(distance_km: float) -> float:
    """Calculates earth curvature error in meters.
    Formula: c = 0.0785 * D^2, where D is in km.
    """
    return 0.0785 * (distance_km ** 2)

def calculate_refraction(distance_km: float) -> float:
    """Calculates atmospheric refraction correction in meters.
    Formula: r = 0.011 * D^2, where D is in km.
    """
    return 0.011 * (distance_km ** 2)

def calculate_combined_correction(distance_km: float) -> float:
    """Calculates combined curvature and refraction correction in meters.
    Formula: c&r = 0.0675 * D^2, where D is in km.
    """
    return 0.0675 * (distance_km ** 2)
```

### (iv) Reduction of levels and correction to the relevant height datum

Hydrographic surveying requires reducing elevations to specialized, water-level-based vertical datums like Lowest Astronomical Tide (LAT) or Mean Lower Low Water (MLLW). When no local tidal benchmarks are available, you must accurately transfer the datum and establish physical reference points.

The process of determining a new elevation from a known benchmark involves calculating the Height of Instrument (HI) by adding the backsight reading to the known elevation, and then subtracting the foresight reading to find the new elevation.

**Python Snippet for Level Reduction:**

```python
def reduce_level(backsight: float, foresight: float, known_elevation: float) -> float:
    """Calculates the new elevation based on a backsight and foresight."""
    height_of_instrument = known_elevation + backsight
    new_elevation = height_of_instrument - foresight
    return new_elevation

# Example:
# Benchmark = 10.0m
# Backsight reading = 1.5m
# Foresight reading = 1.2m
# New elevation will be 10.3m
```

### (v) Calibration requirements and documentation

All equipment utilized in a hydrographic survey must be proven free of systematic errors through rigorous calibration. 

**The Two-Peg Test**
For optical and digital levels, the most critical calibration procedure is the verification of the horizontal line of sight (collimation error). The Two-Peg test involves:
1. Setting up the instrument exactly halfway between two staffs to determine the true height difference (canceling out curvature, refraction, and internal errors).
2. Moving the instrument very close to one staff and taking a second set of readings.
3. Calculating the apparent height difference and comparing it to the true difference to reveal the exact collimation error.

**Documentation and Metadata**
A legal chain of custody for depth data relies entirely on metadata documentation, often adhering to the [IHO S-100](https://en.wikipedia.org/wiki/S-100) or [ISO 19115](https://en.wikipedia.org/wiki/ISO_19115) standards. This includes:
- **Site Reports:** Descriptions and photos of benchmarks.
- **Raw Data:** Unedited files from digital levels.
- **Calibration Certificates:** Proof of instrument calibration.
- **Datum Offset Computations:** Mathematical proof linking the tide sensor to terrestrial benchmarks.

## F1.4b Height reduction

Hydrographic surveys must be conducted in strict accordance with standards (e.g., IHO Publication S-44). Before finalizing elevations for depth reduction, a surveyor must:
1. Isolate blunders.
2. Correct systematic errors (curvature, refraction, collimation).
3. Mathematically distribute remaining random errors through a network adjustment.

### Data Processing Example: SQL Databases
Often, surveyors process large datasets of leveling observations. Using lightweight SQL databases like [SQLite](https://en.wikipedia.org/wiki/SQLite) or [DuckDB](https://duckdb.org/) allows for rapid, reproducible level reduction across many points.

**SQLite Example:**
```python
import sqlite3

# In-memory database for demonstration
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE levelling_data (
        point_id TEXT,
        backsight REAL,
        foresight REAL,
        known_elevation REAL
    )
''')

cursor.execute("INSERT INTO levelling_data VALUES ('Benchmark_2', 1.5, 1.2, 10.0)")

# Calculate new elevation directly in SQL
cursor.execute('''
    SELECT point_id, (known_elevation + backsight - foresight) AS new_elevation
    FROM levelling_data
''')

print(cursor.fetchall()) 
# Output: [('Benchmark_2', 10.3)]
conn.close()
```

**DuckDB Example:**
DuckDB excels at analytical queries and handles dataframes natively.

```python
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('''
    CREATE TABLE levelling_data (
        point_id VARCHAR,
        backsight DOUBLE,
        foresight DOUBLE,
        known_elevation DOUBLE
    )
''')
conn.execute("INSERT INTO levelling_data VALUES ('Benchmark_3', 2.0, 1.0, 15.0)")

result = conn.execute('''
    SELECT point_id, (known_elevation + backsight - foresight) AS new_elevation
    FROM levelling_data
''').fetchall()

print(result)
# Output: [('Benchmark_3', 16.0)]
```