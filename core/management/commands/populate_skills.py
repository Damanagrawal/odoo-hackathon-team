from django.core.management.base import BaseCommand
from core.models import Skill

class Command(BaseCommand):
    help = 'Populate the database with sample skills'

    def handle(self, *args, **options):
        skills = [
            'Programming - Python',
            'Programming - JavaScript',
            'Programming - Java',
            'Web Development',
            'Mobile App Development',
            'Data Science',
            'Machine Learning',
            'UI/UX Design',
            'Graphic Design',
            'Digital Marketing',
            'Content Writing',
            'Photography',
            'Video Editing',
            'Music Production',
            'Language - Spanish',
            'Language - French',
            'Language - German',
            'Cooking',
            'Fitness Training',
            'Yoga Instruction',
            'Public Speaking',
            'Project Management',
            'Financial Planning',
            'Guitar Playing',
            'Piano Playing',
            'Drawing & Sketching',
            'Woodworking',
            'Gardening',
            'Auto Repair',
            'Home Improvement'
        ]

        for skill_name in skills:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created skill: "{skill_name}"')
                )
            else:
                self.stdout.write(f'Skill already exists: "{skill_name}"')

        self.stdout.write(
            self.style.SUCCESS(f'Finished! Total skills in database: {Skill.objects.count()}')
        )
