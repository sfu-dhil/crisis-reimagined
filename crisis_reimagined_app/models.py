import uuid
from django.utils.safestring import mark_safe
from django.db import models
from solo.models import SingletonModel
from polymorphic.models import PolymorphicModel

class Response(PolymorphicModel):
    class Status(models.TextChoices):
        PENDING_REVIEW = 'pending review', 'Pending Review'
        APPROVED = 'approved', 'Approved'
        DENIED_ARCHIVE = 'denied archive', 'Denied (but archived)'

    # fields
    # using a uuid7 for response id.
    # id will be stored in the frontend after response creation in order to retrieve non-pubic responses later
    # uses uuid7 so the id is not guessable but still relatively sequentially (potentially to switch to uuid4 if true random needed)
    id = models.UUIDField(primary_key=True, default=uuid.uuid7)
    status = models.CharField(choices=Status.choices, db_index=True, default=Status.PENDING_REVIEW)

    # write tracking
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'crisis_reimagined_response'
        verbose_name = 'Response'

    def get_full_response(self):
        return ''

    def __str__(self):
        return f'{self.id} [{self._meta.verbose_name}] [{self.status}]'

class KnowledgeResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='What counts as knowledge in this future?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='What has the university become?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_knowledge'
        verbose_name = 'Knowledge'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')

class RestitutionResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='What injustice will the university be forced to address?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='How will this restitution transform the university?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_restitution'
        verbose_name = 'Restitution'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')

class MassificationResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='What population will the university serve?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='How will the university change to accommodate this population?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_massification'
        verbose_name = 'Massification'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')

class TechnologyResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='What new technological crisis will the university face?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='How will the university face this transformation?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_technology'
        verbose_name = 'Technology'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')

class MarketizationResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='how do you see this crisis, continuing, evolving, reemerging?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='how would you like the university to respond?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_marketization'
        verbose_name = 'Marketization'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')

class GeopoliticsResponse(Response):
    # fields
    year = models.IntegerField(verbose_name='In the year', null=True, blank=True)
    question_1 = models.TextField(verbose_name='What key geopolitical transformation will the university need to respond to?', null=True, blank=True)
    question_2 = models.TextField(verbose_name='Who will the university respond?', null=True, blank=True)

    class Meta:
        db_table = 'crisis_reimagined_response_geopolitics'
        verbose_name = 'Geopolitics'

    def get_full_response(self):
        result_parts = []
        if self.year:
            result_parts.append(f'<strong>{self._meta.get_field('year').verbose_name}</strong> {self.year}')
        if self.question_1:
            result_parts.append(f'<strong>{self._meta.get_field('question_1').verbose_name}</strong><br /> {self.question_1}')
        if self.question_2:
            result_parts.append(f'<strong>{self._meta.get_field('question_2').verbose_name}</strong><br /> {self.question_2}')
        return mark_safe('<br /><br />'.join(result_parts) if len(result_parts) > 0 else '')


class Config(SingletonModel):
    responses_enabled = models.BooleanField(verbose_name='Responses enabled?', default=True, db_index=True)

    class Meta:
        db_table = 'crisis_reimagined_config'
        verbose_name = 'Website Config'

    def __str__(self):
        return 'Website Config'