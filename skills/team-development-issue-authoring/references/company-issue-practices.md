# 기능 이슈·하위 테스크 이슈 공개 사례 조사

조사일: 2026-09-20

## 읽는 방법

이 문서는 공개된 기술 블로그·공식 문서에서 확인 가능한 사실만 정리한다. 각 회사의 실제 내부 이슈 제목 형식, 템플릿, 담당자 정책, GitHub/Jira 설정은 공개되지 않은 경우가 많으므로 추정하지 않는다. 따라서 아래 사례는 팀의 템플릿을 그대로 복제하는 대상이 아니라, 기능 이슈와 독립 테스크를 나누는 설계 근거로만 사용한다.

## 국내 빅테크·대기업·유니콘 공개 사례

| 조직 | 공개적으로 확인된 방식 | 이 가이드에 반영한 점 | 한계 |
| --- | --- | --- |
| 카카오 | [Olive Platform 사례](https://tech.kakao.com/posts/424)는 모든 작업을 Jira에 등록해 백로그·짧은 스프린트로 관리하고, 다음 배포의 기능과 위험을 점검한다고 설명한다. | 기능 목표와 실제 작업을 백로그/테스크로 추적하고 위험·의존성을 부모에 남긴다. | 부모-하위 이슈의 정확한 명칭·양식은 공개되지 않았다. |
| 카카오페이 | [Jira 마이그레이션 회고](https://tech.kakaopay.com/post/jira-migration-review/)는 Jira·Wiki 운영, 과제 그룹화, 체크리스트와 테스트 마이그레이션을 기록한다. | 큰 변경은 검증 가능한 작업 단위와 체크리스트로 분해한다. | 일반 기능 이슈의 계층 템플릿을 공개한 자료는 아니다. |
| 네이버 | [NAVER D2 사례](https://d2.naver.com/helloworld/2017402)는 Jira 대시보드에서 컴포넌트별 작업량을 보고, 팀 고유의 이슈 타입·업무 흐름이 필요했다고 설명한다. | 공통 구조는 유지하되 영역 라벨·이슈 타입·흐름은 팀 상황에 맞춘다. | 기능/테스크 제목 규칙은 공개되지 않았다. |
| 토스 | [이슈봇 사례](https://toss.tech/article/22439)는 Slack에서 Jira 이슈를 생성·수정·완료하는 흐름을, [토스플레이스 QA 사례](https://toss.tech/article/41793)는 이슈별 스레드·담당자·템플릿을 설명한다. | 이슈는 실행 맥락에서 빠르게 만들되 담당·상태·논의가 한곳에서 추적되어야 한다. | QA 사례는 장기·복잡 프로젝트에는 한계가 있다고 밝히며, 기능/테스크 계층을 정의하지는 않는다. |
| 우아한형제들 | [대용량특가 프로젝트 사례](https://techblog.woowahan.com/15268/)는 기획·개발의 세부 작업별 티켓, 라벨·컴포넌트·시작/종료일 규칙, 작업 간 선후 관계 추적을 설명한다. [Jira Automation 사례](https://techblog.woowahan.com/23377/)는 생성·상태·할당을 조건 기반으로 자동화한다. | 독립 테스크에는 영역, 기한·의존성, 상태를 분명히 하고 자동화는 규칙이 확정된 뒤 적용한다. | 백엔드·프론트엔드 분리 명칭은 공개되지 않았다. |
| SK텔레콤 / 에이닷 | [Advanced Roadmaps 사례](https://devocean.sk.com/blog/techBoardDetail.do?ID=167293)는 `이니셔티브 → 에픽 → 스토리/작업 → 부작업` 계층과, 목표를 상위 이슈로 두고 action item을 에픽·스토리로 세분화하는 방식을 설명한다. [테스트 관리 사례](https://devocean.sk.com/blog/techBoardDetail.do?id=164332)는 관리 이슈를 부모 링크로 두고 여러 스토리를 연결하는 구조를 설명한다. | 사용자 결과를 부모 기능 이슈로, 독립 실행 단위를 영역별 테스크 이슈로 분리한다. | Jira 구성·명칭은 해당 조직의 특정 프로젝트 설정이다. |
| SK C&C / Devocean 공개 프로젝트 사례 | [GitHub + Zenhub 사례](https://devocean.sk.com/blog/techBoardDetail.do?ID=163408)는 Epic에 개발 이슈를 할당하고, 상태·담당자·스프린트·추정·의존성을 추적한 방식을 설명한다. | GitHub 중심이어도 상위 목표와 개발 티켓 관계, 담당·상태·의존성을 분리해 관리한다. | Zenhub 사용 사례이며 GitHub 기본 기능만의 운영 방식은 아니다. |
| 올리브영, 무신사, 당근, 컬리, 쿠팡, 원티드 | 조사 시점에 각 회사의 공식 기술 채널·공개 GitHub 저장소에서 기능 이슈와 백엔드/프론트엔드 하위 테스크의 구체적 작성 양식을 검증할 1차 자료를 찾지 못했다. | 공개 근거가 없는 내부 규칙을 이 가이드에 귀속하지 않는다. | 비공개 협업 도구 또는 공개되지 않은 운영 방식일 수 있다. |

## 플랫폼의 공개 기능

- [GitHub 공식 문서](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)는 작업 목록 항목을 별도 이슈로 전환해 더 상세한 추적·논의를 할 수 있다고 안내한다.
- [GitHub Copilot 이슈 문서](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/use-copilot-to-create-or-update-issues)는 부모 이슈와 하위 이슈 트리 초안을 만들고, 생성 전에 검토·수정하는 흐름을 안내한다.
- [GitHub 이슈 템플릿 문서](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)는 기능 요청 등 유형별 템플릿과 입력 필드를 저장소에서 구성할 수 있다고 설명한다.

## 결론

공개 사례에서 일관되게 확인되는 것은 특정 제목 접두사가 아니라 다음 네 가지다.

1. 상위 목표와 독립 실행 작업을 분리한다.
2. 각 작업에 담당·상태·의존성·검증 기준을 남긴다.
3. 세부 작업은 직군·컴포넌트·검증 단위에 맞춰 분리한다.
4. 자동 생성·알림은 템플릿과 상태 전이 규칙이 안정된 뒤에 적용한다.

이 스킬은 위 원칙을 `[BE][FEATURE] → [BE][TASK]`와 `[FE][FEATURE] → [FE][TASK]` 구조로 적용한다. 조직의 라벨·담당자·일정·이슈 타입이 다르면 그 저장소의 실제 설정을 우선한다.
