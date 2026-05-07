from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    """A single portfolio project showcased on the site."""

    CATEGORY_CHOICES = [
        ("AI", "Artificial Intelligence"),
        ("ML", "Machine Learning"),
        ("AUTO", "Automation / Agents"),
        ("WEB", "Web Development"),
        ("MEDIA", "Generative Media"),
    ]

    # --- Core info ---
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    summary = models.CharField(
        max_length=200,
        help_text="One-sentence summary shown on cards and the home page.",
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="AI")

    # --- Detailed write-up (interview-ready structure) ---
    business_problem = models.TextField(
        help_text="What real-world problem does this project solve?"
    )
    tools_used = models.CharField(
        max_length=300,
        help_text="Comma-separated list, e.g. 'Python, Django, LangChain, OpenAI API'",
    )
    key_features = models.TextField(
        help_text="One feature per line. Rendered as a bulleted list."
    )
    role_contribution = models.TextField(
        help_text="Your specific role and what you personally built."
    )
    biggest_challenge = models.TextField(
        help_text="The hardest technical or design problem you solved."
    )
    lessons_learned = models.TextField(
        help_text="Key takeaways an interviewer would want to hear."
    )

    # --- Media & links ---
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    link = models.URLField(
        blank=True,
        help_text="GitHub repo, live demo, or video walkthrough URL.",
    )

    # --- Display controls ---
    is_featured = models.BooleanField(
        default=False, help_text="Show on the home page hero section."
    )
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers display first."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    # Helpers used by templates
    def tools_list(self):
        return [t.strip() for t in self.tools_used.split(",") if t.strip()]

    def features_list(self):
        return [f.strip() for f in self.key_features.splitlines() if f.strip()]


class ContactMessage(models.Model):
    """Inbound message from the contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"
