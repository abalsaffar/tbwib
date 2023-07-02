def add_category(name):
    """
    Adds a new category to the database.

    Args:
      name: The name of the new category.

    Returns:
      The created Category object if successful, or None if the category already exists.
    """

    # Check if the category already exists in the database.
    existing_category = Category.query.filter_by(name=name).first()
    if existing_category is not None:
        # Category already exists, return None
        return None

    # Create a new category.
    category = Category(name=name)

    # Save the new category to the database.
    try:
        db.session.add(category)
        db.session.commit()
        return category
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error adding category: {e}")
        db.session.rollback()
        return None
