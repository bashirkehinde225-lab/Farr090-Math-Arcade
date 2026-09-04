import time
from random import choice

from game import layer, processor


def bye(name):
    layer()
    print(
        f"🎮 THANK YOU FOR PLAYING IN THE FARR090 MATH ARCADE!\n"
        f"👋 BYE {name.upper()}!"
    )
    layer()
    exit()
def dim_shapes(name):

    layer()

    print(
        "📐 WELCOME TO THE 2D & 3D SHAPES SUBSECTION\n"
        "📚 This is the area where you learn more about "
        "different types of shapes and their properties."
    )

    layer()

    while True:

        dim_option = input(
            f"So {name}, would you love to go into 2D or 3D? "
        ).lower().strip()

        if dim_option == "2d" or dim_option == "2d shapes":

            general_dim_know2 = [
                "📐 A 2D shape is a flat geometric figure with only length and width, and examples include squares, rectangles, triangles, circles, and polygons.",

                "📏 The perimeter of a 2D shape is the total distance around its boundary; for example, a square has a perimeter of 4 × side, while a rectangle has a perimeter of 2 × (length + width).",

                "🧮 The area of a 2D shape measures the amount of space enclosed inside it; for example, the area of a rectangle is length × width, while the area of a square is side².",

                "🔷 A polygon is a closed 2D shape made entirely from straight line segments, with examples including triangles, quadrilaterals, pentagons, and hexagons.",

                "📐 Angles are formed when two sides meet, and their sizes are measured in degrees; for example, a square has four right angles of 90° each.",

                "⭕ A circle is a curved 2D shape in which every point on its boundary is the same distance from the center; its area is πr² and its circumference is 2πr.",

                "🔺 A triangle has three sides and three angles, and its area can be calculated using ½ × base × perpendicular height, while its perimeter is the sum of its three sides.",

                "🔷 A parallelogram has two pairs of parallel sides, and its area is calculated using base × perpendicular height, while its perimeter is 2 × (base + side).",

                "🔶 A trapezium has at least one pair of parallel sides, and its area is ½ × (a + b) × height, where a and b are the lengths of the parallel sides.",

                "🪞 Symmetry describes how parts of a shape can match each other; for example, a square has four lines of symmetry, while a circle has infinitely many lines of symmetry."
            ]

            for number, concept in enumerate(general_dim_know2, start=1):

                print(f"\n📚 CONCEPT {number}/10")
                print(concept)

                input("\n👉 Press Enter for the next concept...")

            time.sleep(2)
            bye(name)
            break

        elif dim_option == "3d" or dim_option == "3d shapes":

            general_dim_know3 = [
                "🧊 A 3D shape is a solid geometric object that has three dimensions: length, width, and height, with examples including cubes, cuboids, spheres, cylinders, cones, and pyramids.",

                "📦 Volume measures the amount of three-dimensional space occupied by a solid and is expressed in cubic units; for example, the volume of a cuboid is length × width × height.",

                "📐 Surface area measures the total area of all the surfaces covering a 3D object; for example, the surface area of a cube is 6 × side².",

                "🧊 A cube has six equal square faces, twelve equal edges, and eight vertices, with volume = side³ and total surface area = 6 × side².",

                "📦 A cuboid, also called a rectangular prism, has six rectangular faces, and its volume is length × width × height while its total surface area is 2(lw + lh + wh).",

                "🥫 A cylinder has two equal circular bases connected by a curved surface, with volume = πr²h and total surface area = 2πr² + 2πrh.",

                "⚽ A sphere is a perfectly round solid where every point on its surface is the same distance from its center, with volume = 4/3 × πr³ and surface area = 4πr².",

                "🍦 A cone has one circular base and a curved surface that narrows to a single vertex called the apex, with volume = 1/3 × πr²h and curved surface area = πrl.",

                "🔺 A pyramid has a polygonal base and triangular faces that meet at a single apex, with volume = 1/3 × base area × perpendicular height.",

                "📦 Prisms have two identical and parallel polygonal bases connected by rectangular or parallelogram-shaped faces, and their volume can be calculated using base area × perpendicular height."
            ]

            for number, concept in enumerate(general_dim_know3, start=1):

                print(f"\n📚 CONCEPT {number}/10")
                print(concept)

                input("\n👉 Press Enter for the next concept...")

            time.sleep(2)
            bye(name)
            break

        else:

            print(
                f"\n❌ {name}, you have to enter either "
                f"2D or 3D. Please try again!"
            )


def poly(name):

    layer()

    print(
        f"🔷 WELCOME TO THE POLYGON SUBSECTION\n"
        f"📚 This is the area where you learn more about "
        f"different types of polygons and their properties."
    )

    layer()

    print(
        f"So {name}, the following is a deep stack of "
        f"information and knowledge on polygons 📖\n"
    )

    general_poly_know = [

        "🔷 A polygon is a closed two-dimensional shape made entirely from straight line segments, with the line segments meeting at points called vertices.",

        "📏 The sides of a polygon are the straight line segments that form its boundary, and the number of sides determines what type of polygon it is called.",

        "📍 A vertex is a point where two sides of a polygon meet, and the number of vertices in a polygon is always equal to its number of sides.",

        "📐 The interior angles of a polygon are the angles formed inside the shape between two adjacent sides.",

        "🧮 The sum of the interior angles of an n-sided polygon can be calculated using the formula (n - 2) × 180 degrees.",

        "↗️ The exterior angle of a polygon is formed between one side and the extension of an adjacent side, and the exterior angles of any simple polygon add up to 360 degrees.",

        "⭐ A regular polygon has all of its sides equal in length and all of its interior angles equal, while an irregular polygon does not have all these properties.",

        "🔄 A convex polygon has all of its interior angles less than 180 degrees, while a concave polygon has at least one interior angle greater than 180 degrees.",

        "📏 The perimeter of a polygon is the total distance around its boundary, which can be found by adding the lengths of all its sides.",

        "📐 A diagonal is a line segment connecting two non-adjacent vertices of a polygon, and an n-sided polygon has n(n - 3) ÷ 2 diagonals."
    ]

    for number, concept in enumerate(general_poly_know, start=1):

        print(f"\n📚 CONCEPT {number}/10")
        print(concept)

        input("\n👉 Press Enter for the next concept...")

    time.sleep(2)
    bye(name)


def s_learn(name):

    layer()

    print(
        f"📚 WELCOME TO THE GENERAL SHAPES KNOWLEDGE SUBSECTION\n"
        f"This is the area where you learn more about shapes, "
        f"their properties, theorems and pioneers."
    )

    layer()

    list2 = {

        "2 and 3d": "📐 Learning more about 2D and 3D shapes, their theorems and unique properties",

        "polygons": "🔷 Learning and understanding polygon types and properties",

        "pioneers": "🧠 Learning more about great pioneers and philosophers that contributed to this area in Math"
    }

    print("\n📋 Available areas:")

    for key, value in list2.items():
        print(f"🔹 {key} → {value}")

    while True:

        smain_options = input(
            f"\nSo {name}, which of the following areas are we going into today? "
        ).lower().strip()

        if smain_options == "polygons":

            processor()

            print("🔷 Ok then!")

            print(f"💡 Here is another fun fact for you {name}")

            time.sleep(1)

            layer()

            print(f"So {name}, do you know that {get_facts()}")

            layer()

            time.sleep(3)

            poly(name)

            break

        elif smain_options == "2 and 3d" or smain_options == "two and three d shapes":

            processor()

            print("📐 Ok then!")

            print(f"💡 Here is another fun fact for you {name}")

            time.sleep(1)

            layer()

            print(f"So {name}, do you know that {get_facts()}")

            layer()

            time.sleep(3)

            dim_shapes(name)

            break

        elif smain_options == "pioneers":

            processor()

            print("🧠 The pioneers subsection is coming soon!")

            time.sleep(2)

        else:

            print(
                f"❌ Sorry {name}, that service is unavailable."
            )


facts = [

    "🔺 A triangle may look like the simplest polygon, but it is one of the strongest shapes in engineering. Its three sides lock its angles into a fixed structure, which is why triangular frameworks are used in bridges, towers, roof structures, and cranes. If the lengths of all three sides are known, the shape cannot easily deform without one of the sides changing.",

    "📐 The Pythagorean theorem is more than just the famous equation a² + b² = c². It creates a direct connection between the three sides of every right-angled triangle and is used in construction, navigation, physics, computer graphics, engineering, and even calculating distances that cannot be measured directly.",

    "📚 Euclid, who lived around 300 BCE, organized hundreds of geometric ideas into a massive mathematical work called Elements. Instead of simply giving formulas, he built geometry from definitions, assumptions, and logical proofs.",

    "⭕ A perfect circle has infinitely many lines of symmetry because every diameter divides it into two identical halves.",

    "🔢 Archimedes used polygons to estimate the value of π without modern calculators by placing regular polygons inside and outside a circle and increasing the number of their sides.",

    "🧊 Euler discovered a remarkable relationship between the vertices, edges, and faces of many three-dimensional shapes. His formula V - E + F = 2 works for convex polyhedra such as cubes and pyramids.",

    "🔷 There are only five regular convex polyhedra: the tetrahedron, cube, octahedron, dodecahedron, and icosahedron.",

    "⬡ A regular hexagon can cover an entire flat surface without leaving gaps when identical hexagons are placed together. This property is called tessellation.",

    "🏛️ The ancient Egyptians used practical geometry long before modern mathematical notation existed. Geometry helped them measure land, construct buildings, and deal with changes in property boundaries caused by the flooding of the Nile.",

    "⚽ A sphere has the smallest surface area possible for a given volume among all three-dimensional shapes. This mathematical property helps explain why bubbles naturally form spherical shapes when surface tension dominates."
]


def get_facts():
    return choice(facts)


def s_quiz(name):

    processor()
    layer()

    print(
        f"🧮 WELCOME TO THE CALCULATION QUIZ SUBSECTION\n"
        f"This is the area where you answer questions on shapes "
        f"strictly involving calculations."
    )

    q_count_option = int(
        input("⏳ How many seconds should your countdown be: ")
    )

    processor()

    print(f"Get ready {name}, your test starts in: ⏰")

    for i in range(q_count_option, 0, -1):
        print(i)
        time.sleep(1)

    print(f"\n⏰ Time is up {name}, answer the following questions!")

    shape_quiz_questions = {

        "A right-angled triangle has sides of 9 cm and 12 cm. What is the length of the hypotenuse?\n[A] 13 cm  [B] 14 cm  [C] 15 cm  [D] 16 cm": "C",

        "A right-angled triangle has a hypotenuse of 17 cm and one side of 8 cm. What is the length of the other side?\n[A] 12 cm  [B] 13 cm  [C] 14 cm  [D] 15 cm": "B",

        "A rectangle has a diagonal of 25 cm and a length of 24 cm. What is its width?\n[A] 5 cm  [B] 6 cm  [C] 7 cm  [D] 8 cm": "B",

        "An isosceles triangle has two equal sides of 13 cm and a base of 10 cm. What is its perpendicular height?\n[A] 10 cm  [B] 11 cm  [C] 12 cm  [D] 13 cm": "C",

        "A square has a diagonal of 14√2 cm. What is the length of one side?\n[A] 7 cm  [B] 12 cm  [C] 14 cm  [D] 28 cm": "C",

        "A rhombus has diagonals measuring 16 cm and 30 cm. What is the length of each side?\n[A] 15 cm  [B] 16 cm  [C] 17 cm  [D] 18 cm": "C",

        "A right-angled triangle has a hypotenuse of 26 cm and one perpendicular side of 10 cm. Find the other perpendicular side.\n[A] 20 cm  [B] 22 cm  [C] 24 cm  [D] 25 cm": "C",

        "A rectangle has a length of 20 cm and a diagonal of 29 cm. What is its width?\n[A] 19 cm  [B] 20 cm  [C] 21 cm  [D] 22 cm": "C",

        "An equilateral triangle has a perimeter of 48 cm. What is the length of each side?\n[A] 12 cm  [B] 14 cm  [C] 16 cm  [D] 18 cm": "C",

        "A kite has two sides measuring 13 cm each and two other sides measuring 15 cm each. What is its perimeter?\n[A] 48 cm  [B] 52 cm  [C] 54 cm  [D] 56 cm": "B"
    }

    mark = 0

    for question, answer in shape_quiz_questions.items():

        print("\n" + question)

        user_answer = input("Your answer: ").upper()

        if user_answer == answer:

            print("✅ Correct!")
            mark += 1
            print(f"🏆 Score: {mark}/10")

        else:

            print(f"❌ Wrong! The correct answer was {answer}")
            print(f"📊 Score: {mark}/10")

        input("\n👉 Press Enter for the next question...")

    percentage = mark / 10 * 100

    time.sleep(2)

    print(f"\n🎯 You got {percentage}%")

    if percentage >= 50:

        print(f"🎉 Congrats {name}, You passed!")

        time.sleep(2)

        bye(name)

    else:

        print(f"😔 Sorry {name}, you lost!")
        print("💪 Never give up!")

        time.sleep(2)

        bye(name)


def s_guess(name):

    processor()
    layer()

    print(
        f"🔍 WELCOME TO THE GUESSING QUIZ SUBSECTION\n"
        f"This is the area where you answer questions on shapes "
        f"by guessing the shape from its unique properties."
    )

    layer()

    q_count_option = int(
        input("⏳ How many seconds should your countdown be: ")
    )

    processor()

    for i in range(q_count_option, 0, -1):
        print(i)
        time.sleep(1)

    print(f"\n⏰ Time is up {name}, answer the following questions!")

    shape_quiz = {

        "I have four equal sides, four right angles, and my diagonals are equal in length. What shape am I?": "square",

        "I have three sides and three angles. The sum of my interior angles is always 180°. What shape am I?": "triangle",

        "I have four sides, opposite sides are equal and parallel, and all four angles are 90°. What shape am I?": "rectangle",

        "I have four equal sides, but my angles do not have to be 90°. My opposite angles are equal. What shape am I?": "rhombus",

        "I have no straight sides, no vertices, and every point on my boundary is the same distance from my center. What shape am I?": "circle",

        "I have five straight sides and five interior angles. What shape am I?": "pentagon",

        "I have six straight sides and six interior angles. A regular version has all six sides equal. What shape am I?": "hexagon",

        "I have four sides, but only one pair of opposite sides is parallel. My parallel sides are called bases. What shape am I?": "trapezium",

        "I have eight straight sides and eight interior angles. What shape am I?": "octagon",

        "I have four sides, opposite sides are parallel, and my opposite angles are equal. Unlike a rectangle, my angles do not have to be 90°. What shape am I?": "parallelogram"
    }

    mark = 0

    for clues, answer in shape_quiz.items():

        print("\n" + clues)

        user_answer = input("🔍 What shape am I? ").lower().strip()

        if user_answer == answer:

            print("✅ Correct!")

            mark += 1

            print(f"🏆 Score: {mark}/10")

        else:

            print(f"❌ Wrong! The answer was {answer}")

            print(f"📊 Score: {mark}/10")

        input("\n👉 Press Enter for the next question...")

    percentage = mark / 10 * 100

    time.sleep(2)

    print(f"\n🎯 You got {percentage}%")

    if percentage >= 50:

        print(f"🎉 Congrats {name}, You passed!")

        time.sleep(2)

        bye(name)

    else:

        print(f"😔 Sorry {name}, you lost!")

        print("💪 Never give up!")

        time.sleep(2)

        bye(name)


def main_shape(name):

    print(
        f"\n📐 You are now in the Shapes Sphere {name}\n"
        f"💡 Here is a fun fact for you {name}"
    )

    time.sleep(1)

    layer()

    print(f"So {name}, do you know that {get_facts()}")

    layer()

    time.sleep(4)

    print("😎 Cool right!")

    main_list = {

        "shapes quiz": "🔍 Guessing different shapes by their unique properties",

        "calculation quiz": "🧮 Calculating questions involving calculations on shapes",

        "general knowledge": "📚 Understanding the general concepts of shapes, types, theorems, properties, and great pioneers and philosophers"
    }

    print(
        f"\n📋 So {name}, here is a list of my services in this section:"
    )

    time.sleep(1)

    for key, value in main_list.items():
        print(f"🔹 {key} → {value}")

    while True:

        s_main_option = input(
            f"\nSo {name}, which section are you diving into today? "
        ).lower().strip()

        if s_main_option == "general knowledge":

            processor()

            print("📚 Ok then!")

            print(f"💡 Here is another fun fact for you {name}")

            time.sleep(1)

            layer()

            print(f"So {name}, do you know that {get_facts()}")

            layer()

            time.sleep(3)

            s_learn(name)

            break

        elif s_main_option == "calculation quiz":

            processor()

            print("🧮 Ok then!")

            print(f"💡 Here is another fun fact for you {name}")

            time.sleep(1)

            layer()

            print(f"So {name}, do you know that {get_facts()}")

            layer()

            time.sleep(3)

            s_quiz(name)

            break

        elif s_main_option == "shapes quiz":

            processor()

            print("🔍 Ok then!")

            print(f"💡 Here is another fun fact for you {name}")

            time.sleep(1)

            layer()

            print(f"So {name}, do you know that {get_facts()}")

            layer()

            time.sleep(3)

            s_guess(name)

            break

        else:

            processor()

            print(
                f"❌ Sorry {name}, that service is unavailable."
            )

            print("\n📋 Available sections:")

            for key in main_list:
                print(f"🔹 {key}")