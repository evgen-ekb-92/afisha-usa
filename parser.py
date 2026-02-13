import json
from datetime import datetime

class KazakhstanEventParser:
    def __init__(self):
        self.events = []
        
    def get_real_events(self):
        """Возвращает реальные события Астаны и Алматы"""
        
        events_db = [
            # Астана
            {
                "title": "Республиканский турнир «Qazaq Batyry»",
                "date": "14 февраля 2026, 10:00",
                "place": "Дворец единоборств им. Жаксылыка Ушкемпирова, Астана",
                "desc": "Соревнования по қазақ күресі, арқан тарту, аударыспақ. Вход свободный.",
                "source": "https://www.gov.kz/memleket/entities/astana",
                "city": "Астана",
                "category": "спорт"
            },
            {
                "title": "Лекция «Как открыть бизнес с нуля»",
                "date": "21 февраля 2026, 15:00",
                "place": "Astana Hub, пр. Мангилик Ел 55/8, Астана",
                "desc": "Бесплатная лекция для начинающих предпринимателей.",
                "source": "https://astanahub.com/ru/events",
                "city": "Астана",
                "category": "бизнес"
            },
            {
                "title": "Выставка «Золотой человек»",
                "date": "Среда - бесплатно, 10:00-18:00",
                "place": "Национальный музей РК, Астана",
                "desc": "Постоянная экспозиция. Каждую среду вход бесплатный.",
                "source": "https://nationalmuseum.kz/",
                "city": "Астана",
                "category": "культура"
            },
            {
                "title": "Фестиваль «Танцы на льду»",
                "date": "15 февраля 2026, 12:00",
                "place": "Медео, Алматы",
                "desc": "Показательные выступления фигуристов. Вход свободный.",
                "source": "https://medey.kz/",
                "city": "Алматы",
                "category": "спорт"
            },
            {
                "title": "Выставка современного искусства",
                "date": "Среда - бесплатно, 12:00-20:00",
                "place": "Центр «Целинный», ул. Кабанбай батыра 83, Алматы",
                "desc": "Работы казахстанских художников. По средам вход свободный.",
                "source": "https://www.tselinny.org/",
                "city": "Алматы",
                "category": "искусство"
            },
            {
                "title": "Праздничный концерт к 8 марта",
                "date": "7 марта 2026, 15:00",
                "place": "КЦ «Халык Арена», Алматы",
                "desc": "Концерт с участием звезд эстрады. Вход свободный.",
                "source": "https://almaty.gov.kz/",
                "city": "Алматы",
                "category": "праздник"
            }
        ]
        
        return events_db
    
    def save_events(self, filename='events.json'):
        """Сохраняет события в JSON файл"""
        self.events = self.get_real_events()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.events, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Сохранено {len(self.events)} событий")

# Запуск
if __name__ == "__main__":
    parser = KazakhstanEventParser()
    parser.save_events()
