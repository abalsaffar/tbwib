import requests

def add_content(title, link, category_id, sub_category_id, user_id, comment):
    """
    Adds a new content to the database.

    Args:
      title: The title of the new content.
      link: The link of the new content.
      category_id: The ID of the category to which the new content belongs.
      sub_category_id: The ID of the sub-category to which the new content belongs.
      user_id: The ID of the user who created the new content.
      comment: The comment of the new content.

    Returns:
      The created Content object if successful, or None if the link already exists for the same user or there's an error.
    """

    # Check if the link already exists for the same user in the database.
    existing_content = Content.query.filter_by(link=link, user_id=user_id).first()
    if existing_content is not None:
        # Link already exists for the same user, return None
        return None

    # Check if the link is valid.
    try:
        response = requests.get(link)
        if response.status_code != 200:
            # Link is not valid, return None
            return None
    except requests.exceptions.RequestException:
        # Link is not valid, return None
        return None

    # Create a new content.
    content = Content(title=title, link=link, category_id=category_id, sub_category_id=sub_category_id, user_id=user_id, comment=comment)

    # Save the new content to the database.
    try:
        db.session.add(content)
        db.session.commit()
        return content
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error adding content: {e}")
        db.session.rollback()
        return None