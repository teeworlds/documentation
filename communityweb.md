## Actions

### News (v1)

- View
- View archive
- Post comment (forum)

### Journal (v1)

- View
- View archive
- Post comment (forum)

### Downloads (v1:ish, could just be a static page)

- View

### User (v1)

- Create (recapchta protected)
- Search
- Password recovery
- Profile update
- Avatar support

### Forum (v1)

- View Forum
- View Topic
- Create Thread
- Post Reply
- Edit Post
- Search
- Close Thread (moderator, django admin can handle it?)
- Move Thread (moderator, django admin can handle it?)
- Merge / Separate threads (moderator, v+)
- Posts should use bbcode formatting

### Polls (v2)

- Vote

### Groups/Clans (v2)

- Search
- Create
- Profile update
- Join/Add
- Quit/Remove

### Maps (v2)

- Upload
- Post comment (forum)

### Demos (v2)

- Upload
- Post comment (forum)

## Models

- News
	* More or less a special forum
- Journal
	* More or less a special forum
- Downloads
	* Versions etc
- Screenshots
- Post
	* Link to poster (user)
	* Time
	* Last edit
	* Text
- Thread
	* Links to posts
- Forum
- Users
	* Name
	* Badges (dev, mod, donor etc)
	* Personal Description
	* Links to clans
	* Links to uploaded content (demos, maps, screenshots)
	* Links to post on the forums
- Group
	* Links to demos
	* Links to members (users)
- Demos
	* Link to uploader (user)
	* Links to up to 2 groups
	* Links to players (users)
	* Comments
- Map
	* Link to creator/uploader (user)
	* Link to group (can be null)

## Ingame browser

So you can browse demos