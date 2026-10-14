# Example 1 images

Place real case images here, for example `cover.png`, `geometry.png`, or `stress-field.png`.

In `_projects/cantilever.md`, set `img: /assets/img/cases/case-1/cover.png` and update `image_alt` to describe the real cover. The page and benchmark cards already use these fields.

Embed additional images within one of the four case sections:

```html
<figure>
  <img
    class="rsh-case-image"
    src="{{ '/assets/img/cases/case-1/stress-field.png' | relative_url }}"
    alt="Describe the stress component and comparison shown."
  />
  <figcaption>State the stress component, units, conditions, and source.</figcaption>
</figure>
```

These filenames are examples, not existing images or computed results. This README is excluded from the generated site.
