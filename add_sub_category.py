def add_sub_category(name, category_id):
    """
    Adds a new sub-category to the database.

    Args:
      name: The name of the new sub-category.
      category_id: The ID of the category to which the new sub-category belongs.

    Returns:
      The created SubCategory object if successful, or None if the sub-category already exists or there's an error.
    """

    # Check if the sub-category already exists in the database.
    existing_sub_category = SubCategory.query.filter_by(name=name, category_id=category_id).first()
    if existing_sub_category is not None:
        # Sub-category already exists, return None
        return None

    # Create a new sub-category.
    sub_category = SubCategory(name=name, category_id=category_id)

    # Save the new sub-category to the database.
    try:
        db.session.add(sub_category)
        db.session.commit()
        return sub_category
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error adding sub-category: {e}")
        db.session.rollback()
        return None
