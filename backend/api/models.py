from django.db import models

Class Goodthing(models.Model):
    content = models.TextField()
    likes_count = models.IntegerField(default=0)
    not_good_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content[:50]  # 显示前50个字符
    
    class Meta:
        ordering = ['-created_at']  # 按创建时间倒序排列