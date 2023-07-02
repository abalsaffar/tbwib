def edit_content(content_id, title=None, link=None, category_id=None, sub_category_id=None, user_id=None, comment=None):
    """
    Edits an existing content in the database.

    Args:
      content_id: The ID of the content to be edited.
      title: The new title of the content (optional).
      link: The new link of the content (optional).
      category_id: The new ID of the category to which the content belongs (optional).
      sub_category_id: The new ID of the sub-category to which the content belongs (optional).
      user_id: The ID of the user who edited the content (optional).
      comment: The new comment of the content (optional).

    Returns:
      The updated Content object if successful, or None if the content does not exist or there's an error.
    """

    # Check if the content exists in the database.
    content = Content.query.filter_by(id=content_id).first()
    if content is None:
        # Content does not exist, return None
        return None

    # Update the content fields if new values are provided.
    if title is not None:
        content.title = title
    if link is not None:
        content.link = link
    if category_id is not None:
        content.category_id = category_id
    if sub_category_id is not None:
        content.sub_category_id = sub_category_id
    if user_id is not None:
        content.user_id = user_id
    if comment is not None:
        content.comment = comment

    # Save the updates to the database.
    try:
        db.session.commit()
        return content
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error updating content: {e}")
        db.session.rollback()
        return None
