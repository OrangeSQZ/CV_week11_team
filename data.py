import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 읽기
file_path = "cox-violent-parsed_filt_usable.csv"
df = pd.read_csv(file_path)

# 1. 20대 남성 중에서 폭력적인 재범 발생여부(is_violent_recid)가 제일 높은 인종 확인
young_adult_males = df[(df['age'] >= 20) & (df['age'] < 30) & (df['sex'] == 'Male')]
violent_recid_by_race = young_adult_males.groupby('race')['is_violent_recid'].mean().sort_values(ascending=False)

# 2. 아시아 여성 중에서 일반적 재범 발생여부(is_recid)가 제일 높은 나이대 확인
asian_females = df[(df['race'] == 'Asian') & (df['sex'] == 'Female')]
asian_females['age_group'] = pd.cut(asian_females['age'], bins=range(10, 101, 10), labels=[f'{i}~{i+9}' for i in range(10, 100, 10)])
recid_by_age_group = asian_females.groupby('age_group')['is_recid'].mean().sort_values(ascending=False)

# 시각화
plt.figure(figsize=(15, 5))

# 1. 20대 남성 중에서 폭력적인 재범 발생여부가 제일 높은 인종
plt.subplot(1, 2, 1)
sns.barplot(x=violent_recid_by_race.index, y=violent_recid_by_race.values, palette='viridis')
plt.title('Probability of violent recidivism (male in his 20s)')
plt.xlabel('Race')
plt.ylabel('Average probability of recidivism')

# 2. 아시아 여성 중에서 일반적 재범 발생여부가 제일 높은 나이대
plt.subplot(1, 2, 2)
sns.barplot(x=recid_by_age_group.index, y=recid_by_age_group.values, palette='viridis')
plt.title('Typical probability of recidivism (Asian women)')
plt.xlabel('Age Group')
plt.ylabel('Average probability of recidivism')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
