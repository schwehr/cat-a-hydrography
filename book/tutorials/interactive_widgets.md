# Interactive Widgets and Extensions

## Challenge: Engaging the Learner
Students often struggle to internalize complex programming syntax when they can only read about it passively. A static code block doesn't tell a student if they have misunderstood a nuance of the language.

**Problem:** How can we provide immediate, interactive feedback to a student learning a new programming concept without requiring them to set up a local development environment?

## Solution: Syntax Exercises
The TeachBooks framework incorporates interactive **Syntax Exercises** that allow students to practice coding directly within the browser. 

By defining exercises with expected outcomes and dynamic feedback, educators can guide learners step-by-step from confusion to mastery.

### Implementing a Syntax Exercise

Follow these steps to embed a syntax exercise in your Markdown file:

1. **Identify the Concept:** Determine the specific syntax or logic you want the student to practice.
2. **Use the Directive:** Use the `exercise` directive provided by the TeachBooks extension.
3. **Define the Solution:** Provide the expected correct code and the feedback for incorrect attempts.

**Example:**

```markdown
```{exercise} Variable Assignment
:label: my-first-exercise

Assign the value `10` to a variable named `x`.
```

*(Note: The actual syntax depends on the specific extension configuration, refer to the [TeachBooks Manual](https://teachbooks.io/manual) for advanced syntax details).*

By using these interactive elements, you transition from a passive reading experience to an Active Learning environment, fulfilling the problem-based instructional strategy.