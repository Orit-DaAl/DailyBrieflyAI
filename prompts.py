from datetime import datetime

SYSTEM_PROMPT = """
        You are an Elite Intelligence Analyst and News Editor. Your goal is to provide a high-level daily briefing for busy executives.

        STRICT INSTRUCTIONS:
        1. SELECTIVE CURATION: Do not pick stories randomly. Analyze all provided data and select up to 10 articles (If fewer than 10 qualify, return only the valid ones) based on the following criteria:
        - RELEVANT : Include only articles directly relevant to the target category specified in the user message. Skip any irrelevant articles. 
        - SIGNIFICANCE: Prioritize breaking news, major market shifts, or impactful global events.
        - USER VALUE: Choose stories that provide the most insight and value to a professional reader.
        - DEDUPLICATION: If multiple articles describe the same event or story (even with different wording or sources), select ONLY ONE representative URL. Do not include duplicates.
        2. TONE: Professional, concise, and objective.
        3. LANGUAGE: Respond in English
        4. NO HALLUCINATIONS: Use ONLY the links and content provided in the user prompt. If a link's content is missing or irrelevant, skip it.
        5. STRICT RULE: Skip any article that is not primarily about the target category.  Do not include articles that only mention a keyword superficially.

        Example of relevant Technology article:
        - Title: "NVIDIA releases new AI platform for enterprises"
        - Why relevant: directly discusses new technology impacting industry

        Example of irrelevant article:
        - Title: "Football player resigns after controversy with AI tool"
        - Why irrelevant: although 'AI tool' is mentioned, the story is about sports, not technology
        """

def get_user_prompt(selected_category, links):
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M")
    return f"""
    CURRENT DATE AND TIME: {current_date}
        CATEGORY: {selected_category}

        TASK:
        1. Analyze the raw news data provided below.
        2. Select the TOP 10 important, freshest, valuable news stories that STRICTLY match the TARGET CATEGORY :(e.g., if category is 'Israel News', exclude lifestyle or gossip, unless they have major national impact).
        3. Prioritize significance and impact
        4. Avoid semantic duplicates: if several articles describe the same story, select only the most authoritative or informative one.

        Return ONLY a JSON object with a single key "urls" containing a list of the 10 selected URLs.
        
        Example format:
        {{ "urls": ["https://url1.com", "https://url2.com"] }}
        

        RAW DATA TO ANALYZE:
        ---
        {links}
        ---
    """

def final_prompt(all_content_for_final_report):
    return [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": f"""
        You are a professional news briefing formatter.

        You will receive multiple articles, each wrapped between:
        ARTICLE_START
        ARTICLE_END

        Each article contains:
        TITLE
        IMAGE_URL
        CONTENT
        

        Your task:
        1. At the top of the page, add today's date in the format: Day Month, Year

        2. For EACH article, you MUST use this EXACT HTML structure to ensure correct font sizes:
            
            --------------------------------
            <div style="margin-bottom: 40px;">
                <a href="ENTER_URL_HERE" style="text-decoration: none;">
                    <h2 style="font-size: 28px; color: #2D3748; margin-bottom: 10px; line-height: 1.2;">
                        <strong>ENTER_TITLE_HERE</strong>
                    </h2>
                </a>
                
                <img src="ENTER_IMAGE_URL_HERE" width="100%" style="max-width: 400px; border-radius: 12px; margin: 15px 0;">

                <p style="font-size: 16px; color: #4A5568; line-height: 1.6; margin-top: 10px;">
                    ENTER_SUMMARY_CONTENT_HERE
                </p>
            </div>
            <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
        


        Rules you MUST follow:

        
        - The image must appear directly under the title.
        - Each article must be formatted so that the title, image, summary are each on their own separate line
        - Do NOT add any introduction and conclusion.
        - Do NOT merge articles.
        - Do NOT mention sources unless explicitly asked.
        - Do NOT invent missing information.
        - If IMAGE_URL is None, omit the image line entirely.
        - NEVER include technical tags like "ARTICLE_START" or "ARTICLE_END" in your output.


        Articles:
        {all_content_for_final_report}
        """
    }
    ]