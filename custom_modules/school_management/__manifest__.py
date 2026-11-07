{
    "name": "School Management",
    "version": "1.0",
    "summary": "Manage school operations and student information",
    "description": "A comprehensive module for managing school operations, including student enrollment, attendance tracking, grade management, and more.",
    "author": "Al Amin",
    "category": "Education",
    "depends": ["base", "portal", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_information.xml",
        "views/class_information.xml",

    ],
    "installable": True,
    "application": True,

} 