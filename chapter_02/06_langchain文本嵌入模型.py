from langchain_community.embeddings import DashScopeEmbeddings

embed = DashScopeEmbeddings()


print(embed.embed_query("我喜欢你"))