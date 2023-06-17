def edit_sub_category(sub_category_id, name, description):
    """
    Edits an existing sub-category in the database.

    Args:
      sub_category_id: The ID of the sub-category to be edited.
      name: The new name of the sub-category.
      description: The new description of the sub-category.

    Returns:
      The updated SubCategory object if successful, or None if the sub-category does not exist or there's an error.
    """

    # Check if the sub-category exists in the database.
    sub_category = SubCategory.query.filter_by(id=sub_category_id).first()
    if sub_category is None:
        # Sub-category does not exist, return None
        return None

    # Update the sub-category.
    sub_category.name = name
    sub_category.description = description

    # Save the updates to the database.
    try:
        db.session.commit()
        return sub_category
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error updating sub-category: {e}")
        db.session.rollback()
        return None