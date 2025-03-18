## Adding New Worlds

First, choose a name for your new world. This should be as descriptive and creative as you like - this is the name that will appear on the world selection menu. You can use spaces and any other characters that are permitted within filenames. Below we will use name “Flying Cow Party” as an example.

Copy the `Worlds/World One` folder to `Worlds/Flying Cow Party`. You can do this from Godot's FileSystem view by right clicking on `World One` and selecting `Duplicate`. Run the game: you should see “Flying Cow Party” in the world selection menu.

Now, you can adapt the existing sample levels and add new ones within `Worlds/Flying Cow Party`. Only the scene files that start with a number in the filename are considered levels, and a natural order sorting is applied to their filenames. In other words, if you maintain the naming scheme of `1.tscn`, `2.tscn`, `3.tscn` and so on, the levels will play in this order.

Each level should be a numbered scene file, with the following node structure:

- Level (Type: Level)
  - Map (Type: TilemapLayer)

The easiest way to create levels is by painting tiles. Select the Map node. The TileMap panel will open at the bottom. Each level should have the player tile in one cell, and one or more “goober” tiles. These tiles are scenes that become interactive when the level is played.

The first level in the sequence (typically `0.tscn`) is treated as the start screen. This level is treated specially by the game: the player cannot move, and pressing Jump starts the game proper. Similarly, the final level (typically `999.tscn`) is treated as the end screen.

A core part of the game is that the levels wrap around: if the player or enemies move off any of the four sides of the screen, they reappear on the opposite side. For this to work correctly, you currently need to manually copy any ledges that are at the edge of the tile map to the corresponding position just off the other edge of the map. See https://github.com/endlessm/everlasting-candy/issues/19 for more details.

## Customizing your world

### Start, end and level progression screens

1. Copy `Image/Title.png` into your world's folder.

2. Use a graphical editor to make any desired changes to these screens.

3. Open your world's `World.tscn` file in the Editor's 2D view.

4. Select the `Overlay` node from the Scene Dock. In the Inspector, observe where the Sprite2D Texture is shown.

5. From the FileSystem dock, locate your world's modified `Title.png` file. Drag that file to the Sprite2D Texture section of the Inspector.

Now your customised start, end and level progression screens will be used in your world.

### TileSet

1. Copy `Image/Tilemap.png` into your world's folder.

2. Use a graphical editor to make any desired changes to these graphics.

3. Open the first level in your world in the Editor's 2D view.

4. Select the `Map` node from the Scene Dock. In the Inspector, locate the `Tile Set` option under `TileMapLayer`.

5. Click the ⌄ there and select `Save As`. Save the resultant `TileSet.tres` in your world's folder.

6. Click `TileSet` in the bottom pane, and click `Tilemap.png` as shown within. Observe where it shows the `Texture` option under `Setup`.

7. From the FileSystem dock, locate your world's modified `Tilemap.png` file. Drag that file to the Texture section that you just located.

Now your customised tilemap is available for use in your level.

You will also need to apply your customised `TileSet.tres` to all other levels in your world:

1. Open the next level in the Editor's 2D view.

2. Select the `Map` node from the Scene Dock. In the Inspector, locate the `Tile Set` option under `TileMapLayer`.

3. Locate your world's `TileSet.tres` in the FileSystem view.

4. Drag `TileSet.tres` over to the `Tile Set` option in the Inspector that you just located.

### Player

#### Sprite swap

1. Copy `Image/Player.png` to the `Image/Player` subdirectory of your world.

2. Edit the image to your taste. Your edited image must have the same dimensions
   and number of frames as the default.

In the editor, the player will have its default appearance, but when you run the
game, its appearance will follow your changes. If you place more than one sprite
sheet into your world's `Image/Player` directory, a random one will be selected
each time you start a level.

#### Further customisation

If you want to customise the Player further (such as by adding more frames to
its animations) you must make your own copy of the scene:

1. Copy `TileSet.tres` into your world, and apply it to all levels in your world, as above.

2. Copy `Scene/Player.tscn` into your world's folder.

3. Open your world's `TileSet` and replace the `Player` scene in its `Actors`
   section with your world's copy of the scene, taking care to keep its ID the
   same (`1`) as the original.

4. Make any changes you desire to your world's Player scene.

### Goober

Follow the same process as for the `Player`, except for the `Goober` scene.

### Explosion

#### Sprite swap

1. Copy `Image/Explosion.png` to the `Image/Explosion` subdirectory of your world.

2. Edit the image to your taste. Your edited image must have the same dimensions
   and number of frames as the default.

If you place more than one sprite sheet into your world's `Image/Explosion`
directory, a random one will be selected each time an explosion occurs.

#### Further customisation

If you want to customise the explosion further (such as by adding more frames to
its animations) you must make your own copy of the scene:

1. Copy `Scene/Explosion.tscn` into your world's folder.

2. In each of your world's levels, select the root `Level` node; in the inspector, set the `Explosion Scene` property to your world's copy of the scene.

3. Make any changes you desire to your world's Explosion scene.

### Music

1. Open your world's `World.tscn` file in the Editor's 2D view.

2. Select the `Music` node from the Scene Dock.

3. Use the Inspector to customise the music playback options or to use a different audio file.

### Sound effects

1. Open your world's `World.tscn` file in the Editor's 2D view.

2. Select the `Win` or `Lose` Audio node from the Scene Dock.

3. Use the Inspector to customise the playback options or to use a different audio file.

### Falling candy

Put replacement images into the `Image/Candy` subdirectory of your world. They
will fall in a shuffled order when you play your world.

### Background

1. Open your world's `World.tscn` file in the Editor's 2D view.

2. Select the `Background` ColorRect node from the Scene Dock.

3. Use the Inspector to customise the Color property under ColorRect.

Note: the background would still look light yellow when editing each level or when playing each level scene in isolation, but it will look as expected when playing the game and selecting your world from the menu.

## Contributing your world

Once your world is at a suitable point for initial contribution, please submit it to Everlasting Candy as a GitHub Pull Request.

The commits within your Pull Request should consist only of the addition of your world. You must not include any unrelated changes.

When creating your Pull Request, please pay particular attention to the Pull Request title and description. When your contribution is accepted, all commits in your Pull Request will be squashed into a single commit, which will adopt the title and description from the Pull Request. Your Pull Request should have an imperative title such as "Add Flying Cow World", and the description should briefly explain the key features of your contribution and the reasons behind any key decisions. See [How to Write a Git Commit Message](https://cbea.ms/git-commit/) for more details on the basic linguistic and content standards to follow.

If your change adds assets obtained from other sources, they must be appropriately licensed for free usage and redistribution. We prefer assets licensed under Creative Commons. Your Pull Request Description should note exactly where these assets came from, and you should add a `CREDITS.txt` file in the same directory providing appropriate [attribution](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution) for each file e.g.:

> background.png: "Flying Cows" by John Blake is licensed under CC BY 4.0

Please also post a follow-up comment on your Pull Request with screenshots or a video showing your world in action. This is optional but recommended. Showcase your contribution!

Your Pull Request may receive feedback from maintainers and peers. In order to respond to this feedback, you do not need to create a new branch or open a new Pull Request. Please continue working on the same branch, and the existing Pull Request will automatically update. You can either address feedback by creating followup commits (they will later be squashed), or by modifying and force-pushing the original commits.

Once your contribution gets accepted into the main game, it is recommended that you delete your branch from your forked repository and any local clones. This is because the commit squashing process will effectively replace your contribution with a *new* commit with a different ID, so it will be easy to get confused if you keep the old version around.
