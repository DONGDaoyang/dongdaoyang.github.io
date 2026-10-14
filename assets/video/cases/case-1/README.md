# Example 1 videos

Place actual case videos here. MP4 is a suitable starting point; keep files small enough for the repository and page loading.

Embed a video inside a case section (for example Results):

```html
<video controls preload="metadata" playsinline style="width: 100%;">
  <source src="{{ '/assets/video/cases/case-1/process.mp4' | relative_url }}" type="video/mp4" />
  Your browser does not support embedded video.
</video>
```

`process.mp4` is an example filename, not an existing video. Describe what the animation shows and whether it is illustrative or a real simulation. This README is excluded from the generated site.
