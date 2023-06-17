def edit_category(category_id, name, description):
    """
    Edits an existing category in the database.

    Args:
      category_id: The ID of the category to be edited.
      name: The new name of the category.
      description: The new description of the category.

    Returns:
      The updated Category object if successful, or None if the category does not exist or there's an error.
    """

    # Check if the category exists in the database.
    category = Category.query.filter_by(id=category_id).first()
    if category is None:
        # Category does not exist, return None
        return None

    # Update the category.
    category.name = name
    category.description = description

    # Save the updates to the database.
    try:
        db.session.commit()
        return category
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error updating category: {e}")
        db.session.rollback()
        return None