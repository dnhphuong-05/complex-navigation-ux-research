---
title: "UX Navigation Research Dataset — Complex Multi-level Sidebar / Information Architecture"
language: "vi"
version: "1.0"
created_for: "AI CRM multi-level navigation research"
purpose: "Human-readable literature review + machine-readable research dataset for Python analysis"
data_status: "Literature-derived evidence and research-plan schema; NOT raw participant data"
---

# UX Navigation Research Dataset

## 0. Cách dùng file này

File này có 2 mục đích:

1. **Đọc như một literature review** về Navigation / Sidebar / Information Architecture.
2. **Parse bằng Python** để:
   - lọc nghiên cứu theo topic;
   - so sánh phương pháp;
   - tổng hợp biến đo;
   - xây hypothesis;
   - thiết kế Tree Testing / Usability Testing / A/B Testing;
   - nhập dữ liệu nghiên cứu thật của AI CRM về sau.

> Quan trọng: Các con số trong phần `study_records` chỉ được điền khi có bằng chứng từ nguồn đã kiểm tra.  
> Trường chưa xác minh được để `null`, không tự suy đoán.

---

# 1. Case Definition

## 1.1 Bối cảnh

Case nghiên cứu là một hệ thống **AI CRM All-in-One** có navigation dạng left sidebar với nhiều nhóm chức năng cấp 1, mỗi nhóm tiếp tục có nhiều chức năng cấp 2 / cấp 3.

Ví dụ các nhóm hiện tại:

- Tổng quan
- CRM Core
- Phễu bán hàng
- Sản phẩm & Đơn hàng
- Thanh toán & Hợp đồng
- Email Marketing
- Landing & Phễu
- Truyền thông
- Báo cáo & Hiệu suất
- Affiliate
- AI & Tự động hoá
- Kết nối & Dữ liệu
- Nội bộ công ty
- Cài đặt & Bảo mật

## 1.2 Research problem

> Làm thế nào để tổ chức một hệ thống có số lượng chức năng lớn và nhiều lớp sao cho người dùng có thể tìm đúng tính năng nhanh, hiểu rõ cấu trúc và giảm navigation effort?

## 1.3 Không giả định trước

Không được mặc định rằng:

- ít menu hơn luôn tốt hơn;
- sidebar trái luôn tốt nhất;
- càng shallow càng tốt trong mọi context;
- hamburger/collapse luôn tốt hơn;
- search có thể thay thế IA;
- một cấu trúc navigation phù hợp cho mọi role.

Các điểm trên phải được kiểm chứng bằng nghiên cứu.

---

# 2. Core Research Questions

| ID | Research Question |
|---|---|
| RQ01 | Người dùng phân nhóm các tính năng CRM theo mental model như thế nào? |
| RQ02 | Những label/module nào tạo semantic overlap hoặc ambiguity? |
| RQ03 | Breadth và depth của hierarchy ảnh hưởng thế nào đến findability? |
| RQ04 | User thường bắt đầu từ module nào khi thực hiện các task quan trọng? |
| RQ05 | Global + contextual navigation có giúp giảm navigation effort so với một sidebar chứa toàn bộ chức năng không? |
| RQ06 | Những chức năng nào cần luôn visible, những chức năng nào có thể dùng progressive disclosure? |
| RQ07 | Search đang bổ trợ navigation hay đang bù đắp cho IA khó sử dụng? |
| RQ08 | Mental model có khác nhau giữa Sales, Marketing, Operations, Manager và Admin không? |
| RQ09 | Navigation mới có scalable khi số lượng feature tăng không? |
| RQ10 | Sau khi deploy, navigation mới có cải thiện hành vi thực tế không? |

---

# 3. Hypotheses for the CRM Case

```json
[
  {
    "id": "H01",
    "hypothesis": "Hiển thị quá nhiều lựa chọn cấp 1 cùng lúc làm tăng time-to-feature và wrong first click.",
    "primary_metrics": ["time_to_feature_sec", "first_click_correct", "wrong_turns"],
    "test_methods": ["tree_testing", "usability_testing"]
  },
  {
    "id": "H02",
    "hypothesis": "Semantic overlap giữa các sibling categories làm tăng backtracking và indirect success.",
    "primary_metrics": ["backtracks", "direct_success", "first_click_correct"],
    "test_methods": ["tree_testing", "usability_testing"]
  },
  {
    "id": "H03",
    "hypothesis": "Hierarchy sâu hơn làm tăng perceived complexity và navigation effort cho các task tương đương.",
    "primary_metrics": ["time_to_feature_sec", "clicks", "backtracks", "seq_score"],
    "test_methods": ["tree_testing", "usability_testing"]
  },
  {
    "id": "H04",
    "hypothesis": "Global + contextual navigation có thể cải thiện findability so với một sidebar expose toàn bộ hệ thống.",
    "primary_metrics": ["task_success", "first_click_correct", "time_to_feature_sec", "backtracks"],
    "test_methods": ["tree_testing", "usability_testing", "ab_testing"]
  },
  {
    "id": "H05",
    "hypothesis": "Các feature dùng thường xuyên được truy cập nhanh hơn khi có shortcut như Favorites hoặc Recent.",
    "primary_metrics": ["time_to_feature_sec", "navigation_clicks"],
    "test_methods": ["usability_testing", "ab_testing"]
  },
  {
    "id": "H06",
    "hypothesis": "Search nên bổ trợ chứ không thay thế một IA rõ ràng.",
    "primary_metrics": ["search_usage", "search_success", "navigation_success", "search_dependency"],
    "test_methods": ["analytics", "usability_testing", "ab_testing"]
  }
]
```

---

# 4. Literature Dataset

## 4.1 Machine-readable study records

```json
[
  {
    "study_id": "S001",
    "citation_key": "MuranoLomas2015",
    "authors": ["Pietro Murano", "Tracey J. Lomas"],
    "year": 2015,
    "title": "Menu Positioning on Web Pages. Does it Matter?",
    "source_type": "peer_reviewed_article",
    "venue": "International Journal of Advanced Computer Science and Applications",
    "doi": "10.14569/IJACSA.2015.060419",
    "url": "https://doi.org/10.14569/IJACSA.2015.060419",
    "topics": ["menu_position", "left_navigation", "top_navigation", "usability"],
    "sample_size": 56,
    "sample_notes": "Participants aged 18–59 with internet/computer experience; 14 participants per condition.",
    "design": "between_subjects_experiment",
    "conditions": ["left_vertical", "right_vertical", "top_horizontal", "bottom_horizontal"],
    "tasks_count": 6,
    "independent_variables": ["navigation_position", "task"],
    "dependent_variables": ["task_time", "errors", "mouse_clicks", "subjective_opinion"],
    "analysis_methods": ["Kruskal-Wallis", "Mann-Whitney U"],
    "key_findings": [
      "Top and left navigation performed better than poorer-performing placements on errors and mouse clicks in this experiment.",
      "No statistically significant differences in task time were found.",
      "Subjective ratings were broadly aligned with the performance results."
    ],
    "limitations": [
      "Fictitious online-store context rather than enterprise CRM.",
      "Menu-position experiment does not directly answer optimal hierarchy breadth/depth.",
      "Results should not be converted into a universal rule that left navigation is always superior."
    ],
    "relevance_to_crm_case": "Supports treating navigation position as an empirical variable, but does not resolve the multi-level IA problem.",
    "evidence_scope": "direct_experiment"
  },
  {
    "study_id": "S002",
    "citation_key": "YuRoh2002",
    "authors": ["Byeong-Min Yu", "Seak-Zoon Roh"],
    "year": 2002,
    "title": "The effects of menu design on information-seeking performance and user's attitude on the World Wide Web",
    "source_type": "peer_reviewed_article",
    "venue": "Journal of the American Society for Information Science and Technology",
    "doi": "10.1002/asi.10117",
    "url": "https://doi.org/10.1002/asi.10117",
    "topics": ["menu_design", "global_local_navigation", "information_seeking", "searching", "browsing"],
    "sample_size": null,
    "sample_notes": "Sample size not extracted into this dataset version.",
    "design": "comparative_experiment",
    "conditions": ["simple_selection_menu", "global_local_navigation_menu", "pull_down_menu"],
    "independent_variables": ["menu_design"],
    "dependent_variables": ["search_performance", "browsing_performance", "user_attitude"],
    "key_findings": [
      "Menu design affected information-seeking performance.",
      "Pull-down menu showed stronger searching performance in the study context.",
      "Global/local navigation showed stronger browsing performance in the study context."
    ],
    "limitations": [
      "Cyber-shopping mall prototypes.",
      "Older web context.",
      "Specific information structure limits direct transfer to modern CRM."
    ],
    "relevance_to_crm_case": "Important for comparing a single global menu against global + local/contextual navigation.",
    "evidence_scope": "direct_experiment"
  },
  {
    "study_id": "S003",
    "citation_key": "SnowberryParkinsonSisson1983",
    "authors": ["Kathleen Snowberry", "Stanley R. Parkinson", "Norwood Sisson"],
    "year": 1983,
    "title": "Computer display menus",
    "source_type": "peer_reviewed_article",
    "venue": "Ergonomics",
    "doi": "10.1080/00140138308963390",
    "url": "https://doi.org/10.1080/00140138308963390",
    "topics": ["breadth", "depth", "hierarchical_menu", "search_speed", "accuracy"],
    "sample_size": null,
    "sample_notes": "Sample size not extracted into this dataset version.",
    "design": "controlled_menu_experiment",
    "conditions": ["2^6", "4^3", "8^2", "64^1_categorized", "64^1_randomized"],
    "independent_variables": ["menu_breadth", "menu_depth", "organization"],
    "dependent_variables": ["search_speed", "accuracy"],
    "key_findings": [
      "For the tested verbal hierarchies, search speed and accuracy improved as menu breadth increased when categorical organization was preserved."
    ],
    "limitations": [
      "Early computer-menu context.",
      "64-item verbal hierarchy differs substantially from modern SaaS navigation.",
      "Should inform hypotheses, not provide a fixed numeric design rule."
    ],
    "relevance_to_crm_case": "Foundational evidence for testing breadth-vs-depth rather than assuming deeper hierarchy is automatically cleaner.",
    "evidence_scope": "direct_experiment"
  },
  {
    "study_id": "S004",
    "citation_key": "ParkinsonHillSissonViera1988",
    "authors": ["Stanley R. Parkinson", "Martin D. Hill", "Norwood Sisson", "Cynthia Viera"],
    "year": 1988,
    "title": "Effects of breadth, depth and number of responses on computer menu search performance",
    "source_type": "peer_reviewed_article",
    "venue": "International Journal of Man-Machine Studies",
    "doi": "10.1016/S0020-7373(88)80068-3",
    "url": "https://doi.org/10.1016/S0020-7373(88)80068-3",
    "topics": ["breadth", "depth", "responses", "menu_search"],
    "sample_size": null,
    "sample_notes": "Sample size not extracted into this dataset version.",
    "design": "controlled_menu_experiment",
    "conditions": ["2_options_x_6_frames", "4_options_x_3_frames", "upcoming_selections", "modified_upcoming_selections"],
    "independent_variables": ["breadth", "depth", "number_of_responses"],
    "dependent_variables": ["execution_time", "accuracy"],
    "key_findings": [
      "Number of responses was reported as the most important factor affecting execution time.",
      "The highest-accuracy condition was not the fastest, illustrating a speed-accuracy trade-off.",
      "A modified condition balancing response requirements produced the best combined speed/accuracy performance among tested menus."
    ],
    "limitations": [
      "Legacy menu-navigation context.",
      "Binary/category descriptor structures do not map directly to modern sidebars."
    ],
    "relevance_to_crm_case": "Shows that depth alone is not sufficient; number of required interactions is a separate navigation-cost variable.",
    "evidence_scope": "direct_experiment"
  },
  {
    "study_id": "S005",
    "citation_key": "JackoSalvendy1996",
    "authors": ["Julie A. Jacko", "Gavriel Salvendy"],
    "year": 1996,
    "title": "Hierarchical Menu Design: Breadth, Depth, and Task Complexity",
    "source_type": "peer_reviewed_article",
    "venue": "Perceptual and Motor Skills",
    "doi": "10.2466/pms.1996.82.3c.1187",
    "url": "https://doi.org/10.2466/pms.1996.82.3c.1187",
    "topics": ["breadth", "depth", "perceived_complexity", "hierarchical_menu"],
    "sample_size": 12,
    "sample_notes": "Twelve subjects used six hierarchical menus of varying breadth/depth.",
    "design": "within_study_menu_comparison",
    "independent_variables": ["menu_depth", "menu_breadth"],
    "dependent_variables": ["response_time", "accuracy", "perceived_complexity"],
    "key_findings": [
      "Perceived complexity increased significantly as menu depth increased in the tested conditions."
    ],
    "limitations": [
      "Small sample.",
      "Older computer-menu context.",
      "Perceived complexity should be tested again in the target CRM population."
    ],
    "relevance_to_crm_case": "Supports measuring perceived complexity, not only task success and speed.",
    "evidence_scope": "direct_experiment"
  },
  {
    "study_id": "S006",
    "citation_key": "Blackmon2012",
    "authors": ["Marilyn Hughes Blackmon"],
    "year": 2012,
    "title": "Information scent determines attention allocation and link selection among multiple information patches on a webpage",
    "source_type": "peer_reviewed_article",
    "venue": "Behaviour & Information Technology",
    "doi": "10.1080/0144929X.2011.599041",
    "url": "https://doi.org/10.1080/0144929X.2011.599041",
    "topics": ["information_scent", "link_selection", "semantic_similarity", "web_navigation"],
    "sample_size": null,
    "sample_notes": "Sample size not extracted into this dataset version.",
    "design": "theory_and_empirical_web_navigation_research",
    "independent_variables": ["semantic_relationship_between_goal_and_navigation_cues"],
    "dependent_variables": ["attention_allocation", "link_selection"],
    "key_findings": [
      "Navigation choices are strongly related to the information scent provided by available links/cues.",
      "Competing semantically plausible options can affect allocation of attention and link selection."
    ],
    "limitations": [
      "General web-navigation context rather than enterprise CRM.",
      "Should be operationalized in the CRM through label ambiguity, first click, wrong turns and confidence."
    ],
    "relevance_to_crm_case": "Direct theoretical basis for testing labels such as CRM Core, Phễu bán hàng, Sản phẩm & Đơn hàng, and Báo cáo & Hiệu suất for semantic overlap.",
    "evidence_scope": "theory_plus_empirical"
  },
  {
    "study_id": "S007",
    "citation_key": "PerniceBudiu2016",
    "authors": ["Kara Pernice", "Raluca Budiu"],
    "year": 2016,
    "title": "Hamburger Menus and Hidden Navigation Hurt UX Metrics",
    "source_type": "practitioner_quantitative_research",
    "venue": "Nielsen Norman Group",
    "doi": null,
    "url": "https://www.nngroup.com/articles/hamburger-menus/",
    "topics": ["hidden_navigation", "visible_navigation", "discoverability", "mobile", "desktop"],
    "sample_size": 179,
    "sample_notes": "179 participants; 80 mobile and 99 desktop; six websites; UK participants.",
    "design": "remote_quantitative_user_test",
    "independent_variables": ["navigation_visibility", "device_type", "website"],
    "dependent_variables": ["navigation_usage", "discoverability", "task_difficulty", "task_metrics"],
    "key_findings": [
      "Hidden navigation was less discoverable and was used later/less often than visible navigation in the tested conditions."
    ],
    "limitations": [
      "Practitioner research rather than a peer-reviewed journal article.",
      "Websites tested are not the same as an enterprise CRM.",
      "Hamburger navigation is not identical to an expandable desktop sidebar."
    ],
    "relevance_to_crm_case": "Supports explicitly testing collapsed/hidden navigation instead of assuming a collapsed state is cleaner and therefore better.",
    "evidence_scope": "quantitative_practitioner_study"
  },
  {
    "study_id": "S008",
    "citation_key": "Laubheimer2023TreeTesting",
    "authors": ["Page Laubheimer"],
    "year": 2023,
    "title": "Tree Testing: Evaluate Menu Labels and Categories",
    "source_type": "ux_method_guidance",
    "venue": "Nielsen Norman Group",
    "doi": null,
    "url": "https://www.nngroup.com/articles/tree-testing/",
    "topics": ["tree_testing", "information_architecture", "findability", "labels", "directness"],
    "sample_size": null,
    "sample_notes": "Method article, not a single empirical participant study.",
    "design": "methodological_guidance",
    "independent_variables": ["proposed_information_architecture"],
    "dependent_variables": ["direct_success", "indirect_success", "first_click", "time", "directness"],
    "key_findings": [
      "Tree testing isolates navigation hierarchy and labels from visual UI.",
      "It is suitable for evaluating whether users can find key resources in a proposed hierarchy.",
      "Card sorting and tree testing have different purposes: generation versus evaluation."
    ],
    "limitations": [
      "Tree testing removes visual layout/context and therefore cannot replace full usability testing."
    ],
    "relevance_to_crm_case": "Primary method for comparing IA candidates before investing in high-fidelity UI.",
    "evidence_scope": "methodological_guidance"
  },
  {
    "study_id": "S009",
    "citation_key": "TankalaSherwin2024CardSorting",
    "authors": ["Samhita Tankala", "Katie Sherwin"],
    "year": 2024,
    "title": "Card Sorting: Uncover Users' Mental Models for Better Information Architecture",
    "source_type": "ux_method_guidance",
    "venue": "Nielsen Norman Group",
    "doi": null,
    "url": "https://www.nngroup.com/articles/card-sorting-definition/",
    "topics": ["card_sorting", "mental_models", "information_architecture"],
    "sample_size": null,
    "sample_notes": "Method article, not a single empirical participant study.",
    "design": "methodological_guidance",
    "independent_variables": ["card_set", "sorting_method"],
    "dependent_variables": ["user_groupings", "category_labels", "mental_model_patterns"],
    "key_findings": [
      "Card sorting is used to uncover how users conceptually group information.",
      "Its output should inform possible IA structures rather than be copied mechanically into a final menu."
    ],
    "limitations": [
      "Card labels can bias grouping.",
      "Card sorting does not by itself validate final navigation findability."
    ],
    "relevance_to_crm_case": "Suitable for discovering whether Sales, Marketing, Operations and Admin users group CRM functions differently.",
    "evidence_scope": "methodological_guidance"
  },
  {
    "study_id": "S010",
    "citation_key": "Nielsen2004CardSortSample",
    "authors": ["Jakob Nielsen"],
    "year": 2004,
    "title": "Card Sorting: How Many Users to Test",
    "source_type": "ux_method_guidance",
    "venue": "Nielsen Norman Group",
    "doi": null,
    "url": "https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/",
    "topics": ["card_sorting", "sample_size", "information_architecture"],
    "sample_size": null,
    "sample_notes": "Method guidance recommends at least 15 users for card-sorting studies because of variability in mental models.",
    "design": "methodological_guidance",
    "independent_variables": [],
    "dependent_variables": [],
    "key_findings": [
      "Card-sorting studies generally require more participants than small formative usability tests because mental models vary across users."
    ],
    "limitations": [
      "Rule-of-thumb guidance, not a universal statistical sample-size calculation.",
      "Target population heterogeneity should drive actual recruitment."
    ],
    "relevance_to_crm_case": "Useful starting point for recruitment planning; role segmentation may require a larger sample.",
    "evidence_scope": "methodological_guidance"
  }
]
```

---

# 5. Evidence-to-Decision Matrix

| Design Question | Relevant Evidence | What NOT to conclude | What to test in CRM |
|---|---|---|---|
| Left sidebar hay top nav? | S001 | “Left sidebar luôn tốt nhất” | Left sidebar vs alternative global nav only if product context requires it |
| Broad hay deep? | S003, S004, S005 | “Cứ càng rộng càng tốt” | 2–3 IA structures with different breadth/depth but same destination set |
| Global-only hay global + local? | S002 | “Global + local chắc chắn tốt hơn” | Global/contextual candidate vs current sidebar |
| Label có rõ không? | S006 | “Tên ngắn hơn luôn tốt” | First click, wrong paths, confidence, semantic overlap |
| Collapse sidebar? | S007 | “Collapse luôn xấu” | Persistent vs collapsed state in desktop CRM |
| Card sorting dùng để chọn winner? | S009, S010 | Card sorting = final IA | Use it to generate candidate groupings |
| Tree testing có thay usability test? | S008 | Tree testing = full UI validation | Tree test IA trước, usability test interaction sau |

---

# 6. Variable Dictionary for Python Analysis

```json
{
  "task_success": {
    "type": "binary",
    "values": [0, 1],
    "description": "1 nếu participant hoàn thành đúng task."
  },
  "direct_success": {
    "type": "binary",
    "values": [0, 1],
    "description": "1 nếu tìm đúng destination mà không backtrack."
  },
  "first_click_correct": {
    "type": "binary",
    "values": [0, 1],
    "description": "1 nếu lựa chọn cấp đầu tiên đúng expected path."
  },
  "time_to_feature_sec": {
    "type": "continuous",
    "unit": "seconds",
    "description": "Thời gian từ khi task bắt đầu đến khi chọn đúng destination."
  },
  "clicks": {
    "type": "count",
    "description": "Tổng số click navigation trong task."
  },
  "wrong_turns": {
    "type": "count",
    "description": "Số lần participant đi vào nhánh không dẫn đến destination."
  },
  "backtracks": {
    "type": "count",
    "description": "Số lần quay trở lại level trước."
  },
  "search_used": {
    "type": "binary",
    "values": [0, 1],
    "description": "Có dùng search/command palette hay không."
  },
  "search_success": {
    "type": "binary_or_null",
    "values": [0, 1, null],
    "description": "Nếu dùng search, search có đưa tới đúng feature không."
  },
  "seq_score": {
    "type": "ordinal",
    "range": [1, 7],
    "description": "Single Ease Question sau mỗi task."
  },
  "confidence_score": {
    "type": "ordinal",
    "range": [1, 7],
    "description": "Mức tự tin rằng destination/category được chọn là đúng."
  }
}
```

---

# 7. Data Collection Schema — Tree Testing

Dùng block CSV này làm template tạo file dữ liệu thật.

```csv
participant_id,role,task_id,ia_variant,target_node,first_level_clicked,first_click_correct,direct_success,task_success,time_to_feature_sec,wrong_turns,backtracks,path,confidence_score,notes
P001,Sales,T01,Current,Customer,,,,,,,,,,
P001,Sales,T02,Current,Payment,,,,,,,,,,
P002,Marketing,T01,Candidate_B,Customer,,,,,,,,,,
```

### Primary analysis

- Success rate theo `ia_variant`
- Direct success theo `ia_variant`
- First-click accuracy
- Median time-to-feature
- Wrong turns / backtracks
- Breakdown theo `role`
- Task-level confusion matrix:
  - Expected first-level category
  - Actual first-level category

---

# 8. Data Collection Schema — Moderated Usability Testing

```csv
participant_id,role,experience_level,prototype_variant,task_id,task_success,time_sec,first_click_correct,clicks,wrong_turns,backtracks,search_used,search_success,seq_score,quote,observer_note,severity
P001,Sales,Intermediate,A,T01,,,,,,,,,,,,
P001,Sales,Intermediate,A,T02,,,,,,,,,,,,
```

---

# 9. Data Collection Schema — A/B Testing

```csv
user_id,variant,role,event_date,session_id,task_type,workflow_completed,time_to_feature_sec,navigation_clicks,search_used,search_success,error_event
U001,A,Sales,2026-10-01,S001,find_customer,,,,,,
U002,B,Marketing,2026-10-01,S002,create_campaign,,,,,,
```

### Suggested primary outcome

Chỉ chọn **1–2 primary metrics** trước khi chạy:

- `workflow_completed`
- `time_to_feature_sec`

### Secondary metrics

- navigation_clicks
- search_used
- search_success
- error_event

---

# 10. Card Sorting Data Schema

## 10.1 Raw long format

```csv
participant_id,role,card_id,card_label,group_label
P001,Sales,C001,Customer,CRM
P001,Sales,C002,Lead,CRM
P001,Sales,C003,Order,Sales
```

## 10.2 Python outputs nên tạo

- Co-occurrence matrix
- Similarity matrix
- Hierarchical clustering / dendrogram
- Agreement score
- Cluster comparison by role

> Không tự động biến cluster thành final menu. Cluster chỉ là evidence về mental model.

---

# 11. Navigation Audit Schema

```csv
feature_id,feature_name,current_l1,current_l2,current_l3,role_primary,usage_frequency,business_criticality,search_rate,click_rate,avg_time_to_feature,ambiguity_notes
F001,Customer,CRM Core,,,,,,,,,
F002,Order,Sản phẩm & Đơn hàng,,,,,,,,,
F003,Sales Report,Báo cáo & Hiệu suất,,,,,,,,,
```

---

# 12. Recommended Study Sequence

```json
[
  {
    "phase": 1,
    "method": "navigation_audit",
    "goal": "Lập inventory, breadth, depth, labels, role mapping và usage data."
  },
  {
    "phase": 2,
    "method": "user_interviews",
    "goal": "Hiểu top tasks, language, expectations và mental model theo role."
  },
  {
    "phase": 3,
    "method": "card_sorting",
    "goal": "Sinh candidate groupings dựa trên mental model."
  },
  {
    "phase": 4,
    "method": "ia_design",
    "goal": "Tạo ít nhất 2–3 competing IA candidates."
  },
  {
    "phase": 5,
    "method": "tree_testing",
    "goal": "Đo findability của IA mà chưa bị ảnh hưởng bởi visual design."
  },
  {
    "phase": 6,
    "method": "prototype_usability_testing",
    "goal": "Kiểm tra interaction, visibility, progressive disclosure, search, favorites và context."
  },
  {
    "phase": 7,
    "method": "iteration",
    "goal": "Sửa hierarchy, labels và interaction theo evidence."
  },
  {
    "phase": 8,
    "method": "ab_testing",
    "goal": "Đo ảnh hưởng trên production nếu traffic và instrumentation đủ."
  }
]
```

---

# 13. Candidate IA Definitions for Testing

## Candidate A — Current / Broad Sidebar

```text
Overview
CRM Core
Sales
Products & Orders
Payments
Email Marketing
Landing & Funnel
Communication
Reports & Performance
Affiliate
AI & Automation
Integration & Data
Internal
Settings & Security
```

## Candidate B — Domain Grouping

```text
Overview

Sales
  CRM
  Customers
  Orders
  Products
  Payments

Marketing
  Email
  Landing & Funnel
  Communication
  Affiliate

Analytics
  Reports
  Performance

Automation & Data
  AI & Automation
  Integrations

Organization
  Internal
  Settings
  Security
```

## Candidate C — Global + Contextual

```text
GLOBAL
  Overview
  Sales
  Marketing
  Analytics
  Automation & Data
  Organization

WHEN INSIDE SALES
  Sales Overview
  CRM
  Customers
  Orders
  Products
  Payments
```

> Đây là candidate để test, không phải final recommendation.

---

# 14. Example Tree-Test Tasks

| Task ID | Scenario | Expected destination |
|---|---|---|
| T01 | Thêm một khách hàng mới | Customer |
| T02 | Kiểm tra trạng thái thanh toán của một đơn hàng | Payment |
| T03 | Xem doanh thu tháng hiện tại | Sales Report / Revenue Report |
| T04 | Tạo email campaign | Email Campaign |
| T05 | Kết nối CRM với ứng dụng ngoài | Integration |
| T06 | Thay đổi quyền của nhân viên | Permission |
| T07 | Tạo automation gửi email sau khi đơn hàng hoàn thành | Automation |

> Expected path phải được xác định cho từng IA candidate trước khi chạy test.

---

# 15. Example Python: đọc JSON blocks trong Markdown

```python
from pathlib import Path
import re
import json
import pandas as pd

text = Path("ux_navigation_research_dataset.md").read_text(encoding="utf-8")

json_blocks = re.findall(r"```json\s*(.*?)```", text, flags=re.S)

# Block 0 = hypotheses
hypotheses = json.loads(json_blocks[0])

# Block 1 = study records
studies = json.loads(json_blocks[1])
studies_df = pd.json_normalize(studies)

print(studies_df[[
    "study_id",
    "year",
    "title",
    "source_type",
    "sample_size"
]])
```

---

# 16. Example Python: lọc nghiên cứu theo topic

```python
topic = "breadth"

filtered = studies_df[
    studies_df["topics"].apply(
        lambda xs: topic in xs if isinstance(xs, list) else False
    )
]

print(filtered[["study_id", "title", "year", "key_findings"]])
```

---

# 17. Example Python: Tree Testing Summary

```python
import pandas as pd

df = pd.read_csv("tree_test_results.csv")

summary = (
    df.groupby("ia_variant")
      .agg(
          participants=("participant_id", "nunique"),
          task_success_rate=("task_success", "mean"),
          direct_success_rate=("direct_success", "mean"),
          first_click_accuracy=("first_click_correct", "mean"),
          median_time_sec=("time_to_feature_sec", "median"),
          mean_wrong_turns=("wrong_turns", "mean"),
          mean_backtracks=("backtracks", "mean")
      )
      .reset_index()
)

print(summary)
```

---

# 18. Example Python: Compare Roles

```python
role_summary = (
    df.groupby(["ia_variant", "role"])
      .agg(
          success_rate=("task_success", "mean"),
          first_click_accuracy=("first_click_correct", "mean"),
          median_time_sec=("time_to_feature_sec", "median"),
          mean_backtracks=("backtracks", "mean")
      )
      .reset_index()
)

print(role_summary)
```

---

# 19. Statistical Analysis Guidance

Không chọn statistical test chỉ vì “thường dùng”.

Trước hết xác định:

- independent vs repeated measures;
- sample size;
- distribution;
- metric type;
- multiple tasks per participant;
- role differences;
- missing data.

Ví dụ:

| Question | Possible analysis |
|---|---|
| Success rate A vs B | Chi-square / Fisher's exact / logistic model |
| Time A vs B | t-test nếu phù hợp; Mann–Whitney nếu independent & non-normal; mixed model nếu repeated tasks |
| 3 IA variants | ANOVA / Kruskal–Wallis tùy assumptions |
| Task success có role + variant | Logistic regression / mixed-effects logistic model |
| Time có repeated tasks | Linear mixed-effects / robust alternative |
| First-click destination | Contingency table + confusion matrix |

> Nếu cùng một participant thực hiện nhiều task, các observation không độc lập.  
> Khi dataset đủ lớn, mixed-effects models phù hợp hơn việc coi mọi row là độc lập.

---

# 20. Research Quality Rules

1. Không biến correlation thành causation.
2. Không dùng chỉ `task_success` để kết luận navigation tốt.
3. Luôn xem:
   - directness;
   - first click;
   - time;
   - wrong turns;
   - backtracking.
4. Phân tích theo role.
5. Tách:
   - IA problem;
   - label problem;
   - visual/interaction problem.
6. Không chọn final design từ card sorting alone.
7. Tree testing phải đi trước UI test nếu mục tiêu là đánh giá IA.
8. A/B testing không thay thế qualitative research.
9. Không dùng một paper cũ để đặt quy tắc cứng kiểu “menu chỉ được X items”.
10. Mọi recommendation phải trace được về:
    - literature evidence;
    - user evidence;
    - behavioral metric.

---

# 21. Source List

1. Murano, P., & Lomas, T. J. (2015). *Menu Positioning on Web Pages. Does it Matter?* International Journal of Advanced Computer Science and Applications, 6(4). DOI: 10.14569/IJACSA.2015.060419  
   https://doi.org/10.14569/IJACSA.2015.060419

2. Yu, B.-M., & Roh, S.-Z. (2002). *The effects of menu design on information-seeking performance and user's attitude on the World Wide Web.* Journal of the American Society for Information Science and Technology, 53(11), 923–933. DOI: 10.1002/asi.10117  
   https://doi.org/10.1002/asi.10117

3. Snowberry, K., Parkinson, S. R., & Sisson, N. (1983). *Computer display menus.* Ergonomics, 26(7), 699–712. DOI: 10.1080/00140138308963390  
   https://doi.org/10.1080/00140138308963390

4. Parkinson, S. R., Hill, M. D., Sisson, N., & Viera, C. (1988). *Effects of breadth, depth and number of responses on computer menu search performance.* International Journal of Man-Machine Studies, 28(6), 683–692. DOI: 10.1016/S0020-7373(88)80068-3  
   https://doi.org/10.1016/S0020-7373(88)80068-3

5. Jacko, J. A., & Salvendy, G. (1996). *Hierarchical Menu Design: Breadth, Depth, and Task Complexity.* Perceptual and Motor Skills, 82(3_suppl). DOI: 10.2466/pms.1996.82.3c.1187  
   https://doi.org/10.2466/pms.1996.82.3c.1187

6. Blackmon, M. H. (2012). *Information scent determines attention allocation and link selection among multiple information patches on a webpage.* Behaviour & Information Technology, 31(1), 3–15. DOI: 10.1080/0144929X.2011.599041  
   https://doi.org/10.1080/0144929X.2011.599041

7. Pernice, K., & Budiu, R. (2016). *Hamburger Menus and Hidden Navigation Hurt UX Metrics.* Nielsen Norman Group.  
   https://www.nngroup.com/articles/hamburger-menus/

8. Laubheimer, P. (2023; reviewed 2026). *Tree Testing: Evaluate Menu Labels and Categories.* Nielsen Norman Group.  
   https://www.nngroup.com/articles/tree-testing/

9. Tankala, S., & Sherwin, K. (2024). *Card Sorting: Uncover Users' Mental Models for Better Information Architecture.* Nielsen Norman Group.  
   https://www.nngroup.com/articles/card-sorting-definition/

10. Nielsen, J. (2004). *Card Sorting: How Many Users to Test.* Nielsen Norman Group.  
    https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/

---

# 22. Recommended Next Data Files

Sau file literature này, nên tạo tiếp 4 file riêng:

```text
01_navigation_inventory.csv
02_card_sort_raw.csv
03_tree_test_results.csv
04_usability_test_results.csv
05_ab_test_events.csv
```

File Markdown này giữ vai trò **research dictionary + literature evidence + analysis specification**.

Các CSV giữ **raw data**.

Đây là cấu trúc phù hợp hơn việc nhét toàn bộ participant data vào Markdown.
